class Solution {
private:
    unordered_map<string_view, vector<string_view>> from; // word -> parents,可以改造成to的吗?
    vector<vector<string>> answers;
public:
    vector<vector<string>> findLadders(string beginWord, string endWord,
                                       vector<string>& wordList) {
        if (wordList.empty()) {
            return {};
        }
        unordered_set<string_view> words{wordList.begin(), wordList.end()};
        unordered_set<string_view> level{beginWord};
        unordered_set<string_view> nextLevel;
        // 正向bfs
        bool found = false;
        while (!level.empty()) {
            for (auto it = level.begin(); it != level.end();
                 ++it) {
                string word{*it};
                // 层序遍历必然有当前节点到beginWord是最短路径
                // erase掉,避免构建不必要的路径较长的链接
                words.erase(word);
                for (int i = 0; i < word.size(); ++i) {
                    const char original = word[i];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c == original) {
                            continue;
                        }
                        word[i] = c;
                        auto wordIt = words.find(string_view{word});
                        if (wordIt == words.end()) {
                            // 不再wordList中或者已经移除
                            continue;
                        }
                        if (word == endWord) {
                            found = true;
                        }
                        // 枚举的修改存在wordList中,且之前没被加入level
                        if (level.find(string_view{word}) == level.end()) {
                            nextLevel.insert(*wordIt);
                            from[*wordIt].emplace_back(*it);
                        }
                    }
                    word[i] = original;
                }
            }
            if (found) {
                break;
            }
            level.swap(nextLevel);
            nextLevel.clear();
        }
        if (!found) {
            return {};
        }
        vector<string> path{endWord};
        dfs(path, beginWord, endWord);
        return answers;
    }
    void dfs(vector<string>& path, string_view beginWord, string_view endWord) {
        if (beginWord == endWord) {
            answers.push_back(vector<string>(path.rbegin(), path.rend()));
            return;
        }
        for (auto parent : from[endWord]) {
            path.emplace_back(parent);
            dfs(path, beginWord, parent);
            path.pop_back();
        }
    }
};
