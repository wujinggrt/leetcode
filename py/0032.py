class Solution:
    def dpLongestValidParentheses(self, s: str) -> int:
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
        #
        #   时间、空间  复杂度 O(n)
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

    def longestValidParentheses(self, s: str) -> int:
        """
        最佳思路应该是使用栈。遍历时可以根据过往来判断当前是否有效。记录有效匹配括号数量即可。

        巧妙设计和见解：开始前令栈底预先保存一个 '(' 下标 -1，作为哨兵。用于检查遇到的第一个不匹配的 ')'，
        及时处理和重新清零计数。设置新的哨兵，检查下一个不匹配的 ')'。哨兵设计思路，一般是多设计一个
        能够匹配到目标的对象，方便检测。

        这是非常值得学习的思路，用哨兵或占位，检查第一个出现不匹配，或者推广来说，检查第一个出现异常的地方。
        然后及时处理。

        遍历到 '(' 时，将下标入栈。
        遍历到 ')' 时，直接弹栈。弹栈后，
            如果栈非空，那么栈顶的元素下标是未匹配的左括号，记为 v。即当前括号 ')' 下标为 m。于是有
            区间 (v, m] 匹配到括号。当前有效括号数量是 m - v 个。
            如果栈空，说明弹出了哨兵，代表当前有括号不匹配。于是把当前下标作为哨兵，再次入栈。

        洞察栈的**规律**，用不同方法表达，优化空间到 O(1)。我们可以不用栈，使用两个计数器即可。观察规律，
        栈中总是保存 "("，每当匹配到 ")" 时逐个弹出。一旦 ")" 数量过多，便认为无效。

        于是，引出了最后的方案，使用两个变量模拟如此关系的栈。需要从左往右扫描，也需要从右往左扫描。
            - 从左往右扫描时，以 left 必须大于等于 right。否则右侧括号，找不到左括号来匹配。
              但是，从左往右扫描，会漏掉一种情况。比如 "()(()" 总是满足 left >= right，但长度是 2
              所以需要从右扫描一遍。
            - 从右向左扫描。
        一左一右，将两个情况左右限制在最大值上。
        """
        left, right, max_length = 0, 0, 0
        for i, c in enumerate(s):
            if c == "(":
                left += 1
            else:
                right += 1
            # 匹配到最后一个 ")"，再多便失效了
            if left == right:
                max_length = max(max_length, 2 * left)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == "(":
                left += 1
            else:
                right += 1
            # 匹配到最后一个 ")"，再多便失效了
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left, right = 0, 0
        return max_length