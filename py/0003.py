class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding windows
        # 思路，直接记录窗口字符出现次数，滑动
        # table = [0 for i in range(256)]
        # exclusive_left = -1
        # longest = 0
        # for i in range(len(s)):
        #     table[ord(s[i])] += 1
        #     while table[ord(s[i])] > 1:
        #         exclusive_left += 1
        #         table[ord(s[exclusive_left])] -= 1
        #     longest = max(longest, i - exclusive_left)
        # 思路二，建立字符：索引的映射表，遇见重复的，直接从重复的索引起始下一个再计算长度，并更新
        table = [-1 for i in range(256)]
        exclusive_left = -1
        longest = 0
        for i, c in enumerate(s):
            if table[ord(c)] != -1 and exclusive_left < table[ord(c)]:
                # exclusive_left只能增大，不能减少
                exclusive_left = table[ord(c)]
            table[ord(c)] = i
            longest = max(longest, i - exclusive_left)
        return longest