class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i, c_p in enumerate(p, start=1):
            if c_p != "*":
                break
            dp[0][i] = True
        for i, c_s in enumerate(s, start=1):
            for j, c_p in enumerate(p, start=1):
                if c_p == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = (c_s == c_p or c_p == "?") and dp[i-1][j-1]
        return dp[-1][-1]