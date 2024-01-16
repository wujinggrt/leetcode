struct KeyNode;

struct CountNode {
    int count;
    list<KeyNode> keys;
};

struct KeyNode {
    int key;
    list<CountNode>::iterator countIt;
};

struct ValueNode {
    int value;
    list<KeyNode>::iterator keyIt;
};

class LFUCache {

    unordered_map<int, ValueNode> values_;
    list<CountNode> counts_;
    const int maxSize_;

    void incCount(decltype(values_)::iterator it) {
        auto keyIt = it->second.keyIt;
        auto countIt = keyIt->countIt;
        auto& keys = countIt->keys;
        auto nextCountIt = countIt;
        ++nextCountIt;
        // 到达末尾或者下一个count被删除
        if (nextCountIt == counts_.end() || nextCountIt->count != countIt->count + 1) {
            nextCountIt = counts_.insert(nextCountIt, CountNode{countIt->count + 1});
        }
        // 插入新的count列表，更新values_中的值和KeyNode中的值，删除原来keys中的节点
        keyIt->countIt = nextCountIt;
        it->second.keyIt = nextCountIt->keys.insert(nextCountIt->keys.end(), *keyIt);
        keys.erase(keyIt);
        // 移除节点后，如果链表空了，删除整个链表
        if (keys.empty()) {
            counts_.erase(countIt);
        }
    }

public:
    LFUCache(int capacity) : maxSize_{capacity} {

    }
    
    int get(int key) {
        auto it = values_.find(key);
        if (it == values_.end()) {
            return -1;
        }
        incCount(it);
        return it->second.value;
    }
    
    void put(int key, int value) {
        auto it = values_.find(key);
        if (it != values_.end()) {
            it->second.value = value;
            incCount(it);
            return ;
        }
        if (values_.size() == maxSize_) {
            // 移除出现最少的节点
            auto& keys = counts_.front().keys;
            values_.erase(keys.front().key);
            keys.erase(keys.begin());
            if (keys.empty()) {
                counts_.pop_front();
            }
        }
        // 插入
        auto first = counts_.begin();
        if (first == counts_.end() || first->count != 1) {
            first = counts_.insert(first, CountNode{1});
        }
        auto keyIt = first->keys.insert(first->keys.end(), KeyNode{key, first});
        values_.insert(std::make_pair(key, ValueNode{value, keyIt}));
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
