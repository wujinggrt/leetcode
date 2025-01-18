class Solution:
    def isPalindrome(self, s: str, left: int, right: int) -> int:
        if left == -1 or right == len(s):
            return -1
        if s[left] != s[right]:
            return -1
        further_count = self.isPalindrome(s, left - 1, right + 1)
        return max(right - left + 1, further_count)

    def isPalindrome2(self, s: str, left: int, right: int) -> int:
        i, j = left, right
        while i > -1 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1

    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i, _ in enumerate(s):
            count1 = self.isPalindrome2(s, i, i)
            count2 = 0
            if i != len(s) - 1 and s[i] == s[i + 1]:
                count2 = self.isPalindrome2(s, i, i + 1)
            if count1 > right - left + 1:
                left = i - count1 // 2
                right = i + count1 // 2
            if count2 > right - left + 1:
                left = i - count2 // 2 + 1
                right = i + count2 // 2
        return s[left : right + 1]

# 循环版本
class Solution:
    def expand(self, s: str, index: int) -> str:
        i, j = index, index
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        left, right = i + 1, j - 1
        i, j = index, index + 1
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        i += 1
        j -= 1
        if (right - left) > (j - i):
            return s[left : right + 1]
        return s[i : j + 1]

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i, _ in enumerate(s):
            tmp = self.expand(s, i)
            ans = tmp if len(tmp) > len(ans) else ans
        return ans