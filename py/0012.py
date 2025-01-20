class Solution:
    def intToRoman(self, num: int) -> str:
        # 如果不是在 4 或 9 开始的值，选择这个值能够减去的最大表达，用这个值追加到结果，
        #   剩余的值继续执行；
        # 如果值以 4 或 9 开始，使用 subtractive form 表达，规则是一个减数符号紧挨着的被减数的符号，比如
        #   4 是 I 减数由 V 被减数减去。
        # 10 的次方可以用至多三次连续的符号表示。比如 I, X, C, M。5 不能。超过 4 次则用 subtractive form。
        # 思路，从个位数开始处理，按照上面的开始处理。处理规则如上。以 5 为单位来取余数，便可处理。
        # 使用相反的形式
        symbols = ["I", "V", "X", "L", "C", "D", "M", "#"]  # # for dummy
        base = 0  # 代表处理到多少次方的数据
        res = list()
        while num != 0:
            n = num % 10
            tmp = []
            if n == 4 or n == 9:
                tmp = [symbols[base], symbols[base + (n // 4)]]
            else:
                tmp = [symbols[base + 1]] * (n // 5)
                tmp += [symbols[base]] * (n % 5)
            res += reversed(tmp)
            num = num // 10
            base += 2
        return "".join(reversed(res))