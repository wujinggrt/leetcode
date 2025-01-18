class Solution:
    def match(self, s: str, p: str, i: int, j: int) -> bool:
        if i == 0:
            return False
        if p[j - 1] == ".":
            return True
        return s[i - 1] == p[j - 1]

    def isMatch(self, s: str, p: str) -> bool:
        # dp，状态：f[i][j] 表示 s 前 i 字符与 p 前 j 字符匹配
        # 转移方程如下，根据 p[j]：
        # matches(x, y) 判断两字符是否匹配，或者 y 是 .
        # p[j] 为 *，f[i][j] = f[i-1][j] or f[i][j-2] if matches(s[i], p[j-1]) else f[i][j-2]
        # p[j] 为 小写字符或 ., f[i][j] = f[i-1][j-1] if matches(s[i], p[j]) else False
        # 解释：
        # 1. 当 p[j] 为 *, 第 j-1 个字符匹配 0 次，即不匹配情况下，把 p 的匹配在 j-1 j 处当 0 次匹配。
        #    于是，f[i][j] = f[i][j-2]
        # 2. 匹配 1,2,3... 次情况下，有 f[i][j] = f[i-1][j-2] if s[i]==p[j-1]
        #    f[i][j] = f[i-2][j-2] if s[i-1]==s[i]==p[j-1], ...
        #    如此编程比较麻烦，所以把匹配 1,2,3... 次当做 + 的语义考虑，本质为两种情况：
        #    p[j] 相当于 +，s[i] 与 p[j-1] 匹配之后，
        #    1) 考察 s[i-1] 是否继续进行匹配 p[0..j], 消去了最后一个s[i]影响，此时为 True，
        #       考察前面情况，对应 f[i-1][j], 如此递归地直到 + 只匹配一个的情况。
        #    2) 如果不能匹配，放弃匹配，当做 + 只匹配到 1 个字符的情况，此时为 True，于是参考前面是否匹配，
        #       即可对应 f[i][j-2]，把 p 中 j-1 和 j 字符当做
        #       0 次匹配处理
        #    f[i][j] = (f[i-1][j] or f[i][j-2]) if s[i]==p[j-1] else f[i][j-2]

        m, n = len(s), len(p)
        # f 是 len(s) + 1 x len(p) + 1 的，多一个代表 0
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                # j 从 1 开始，对 p 使用 j - 1 下标是为了对齐 f 从 1 开始的下标
                if p[j - 1] == "*":
                    # 是否会出现 * 在第一个 p 中的字符，即 pattern 格式不正确？暂时不考虑
                    f[i][j] |= f[i][j - 2]
                    if self.match(s, p, i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if self.match(s, p, i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]