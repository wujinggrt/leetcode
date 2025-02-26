class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp: dp[i] 表示 s[i] 结尾有效括号子串长度
        # s[i] == '('，则 dp[i] = 0，因为以 '(' 结尾子串不可能有效。
        # s[i] == ')'，则检查前一个字符：
        #   若 s[i-1] == '(', dp[i] = dp[i-2] + 2
        #   若 s[i-1] == ')', 需要检查，以 s[i-1] 为结尾的有效括号区间外，是否有一个 ( 配对。
        #       比如 (()) 中，第二个 ) 需要检查前一个 ) 对应的有效。比如第二个 ( 左侧有一个对应它。
        #       如果有对应，那么已经确定了 dp[i-1] + 2 个有效括号，接下来再向前考察即可。
        #       dp[i-1] 代表以 s[i-1] 结尾的有效括号数量。
        #
        #       检查 s[i - dp[i-1] - 1] == '('，dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
        #       否则，dp[i] = 0，不匹配。
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        max_len = 0
        for i, c in enumerate(s[1:], 1):
            if s[i] == "(":
                dp[i] = 0
            else:  # s[i] == ')'
                if s[i - 1] == "(":
                    # ()
                    dp[i] = (0 if i < 2 else dp[i - 2]) + 2
                else:
                    # ))
                    previous_pair = i - dp[i - 1] - 1
                    if previous_pair >= 0 and s[previous_pair] == "(":
                        dp[i] = dp[i - 1] + 2
                        if previous_pair > 0:
                            dp[i] += dp[previous_pair - 1]
            max_len = max(max_len, dp[i])
        return max_len