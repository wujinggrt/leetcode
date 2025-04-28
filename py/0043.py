class Solution:
    def add_char(self, target: list[int], num: int, index: int) -> None:
        n = num + target[index]
        target[index] = n % 10
        if n > 9:
            self.add_char(target, n // 10, index - 1)

    def multiply(self, num1: str, num2: str) -> str:
        """字符串相乘。首先确定数字有多少位，再确定相乘后的结果有多少位，初始化如此位数的 0，把每个相乘的结果逐渐相加。
        记 num1 和 num2 分别长度为 n, m，结果 res 长度可能是 n+m 或 n+m-1
        比如，num1 = 123， num2 = 456，从左往右地处理，
        1 的部分代表 100 * 456，45600 加到 res，从左往右，代表从第 n+m-(n-2) 处开始
        2 的部分代表 20 * 456
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n, m = len(num1), len(num2)
        res = [0] * (n + m)
        for i, c1 in enumerate(num1):
            for j, c2 in enumerate(num2):
                # n + m - 1: res 的最后一个位置
                # n - 1 - i: num1 当前位置幂
                # m - 1 - j: num2 当前位置
                # index 应当放置在 n + m - 1 - (n - 1 - i) - (m - 1 - j)，即 i + j + 1
                index = 1 + i + j
                tmp = int(c1) * int(c2)
                self.add_char(res, tmp, index)
        res_num = 0
        for num in res if res[0] != "0" else res[1:]:
            res_num = res_num * 10 + num
        return str(res_num)
        

