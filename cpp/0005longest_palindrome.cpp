class Solution {

    struct Palindrome {
        int pos;
        int count;
    };

    Palindrome expandCenter(string_view sv, int index) const {
        // 一个元素向两侧扩展
        Palindrome maxRes{index, 1};
        for (int i = index, j = index; i >= 0 && j < sv.size(); --i, ++j) {
            if (sv[i] != sv[j]) {
                break;
            }
            maxRes.pos = i;
            maxRes.count = j + 1 - i;
        }
        for (int i = index, j = index + 1; i >= 0 && j < sv.size(); --i, ++j) {
            if (sv[i] != sv[j]) {
                break;
            }
            if (const int count = j + 1 - i; maxRes.count < count) {
                maxRes.pos = i;
                maxRes.count = count;
            }
        }
        return maxRes;
    }

public:
    string longestPalindrome(string s) {
        /*
        状态P(i,j)代表s[i..j]为回文。初始状态为P(i,i)=true, P(i,i+1)=Si==Si+1.
        状态转移的方式由两个基本状态扩展到整条链.
        dp状态转移为:P(i,j)=P(i+1,j−1)∧(Si==Sj), base case为
        dp方法的状态转移为:P(i,j)←P(i+1,j−1)←P(i+2,j−2)←⋯←某一边界情况
        发现状态 P(i,j) 是由 P(i+1,j-1) 等推导而来，最终是一边界情况。一旦 P(i,j) 确定，
        它的值不会被修改。同时，P(ij)的链仅仅有此一条，base case要么是从P(i'i')推导而来，
        要么从 P(i'i'+1) 推导而来，即长度为1或者2的回文中心，不会存在其他情况。
        我们进一步观察，可以看到只要其中一个状态为False，则会导致从此处往下推导的状态为False.
        整条链以此为分界点，全部为false。我们可以做出剪枝。
        重要的Insight是我们只用枚举长度为1和2的回文中心，由此处开始扩展至最长回文，
        并用两个变量记录当前最长回文情况。
        */
        const int n = s.size();
        Palindrome maxRes{0, -1};
        for (int i = 0; i != n; ++i) {
            const auto candidate = expandCenter(s, i);
            if (maxRes.count < candidate.count) {
                maxRes = candidate;
            }
        }
        return s.substr(maxRes.pos, maxRes.count);
    }
};
