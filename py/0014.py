class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = [""]
        if len(strs[0]) == 0:
            return ""
        for i, c in enumerate(strs[0]):
            for s in strs:
                if len(s) == i or s[i] != c:
                    return "".join(res)
            res.append(c)
        return "".join(res)