class Solution:
    def reverse(self, x: int) -> int:
        # 使用十进制存储，或者二进制存储
        if x == 0:
            return 0
        MIN, MAX = -1 << 31, (1 << 31) - 1
        MIN_BOUND = (MIN - (MIN % 10 - 10)) // 10
        MIN_BOUND_OFFSET = MIN % 10 - 10
        MAX_BOUND = MAX // 10
        MAX_BOUND_OFFSET = MAX % 10
        positive = True if x > 0 else False
        res = 0
        while x != 0:
            if positive:
                digit = x % 10
                # 先检查
                if res > MAX_BOUND or (res == MAX_BOUND and digit > MAX_BOUND_OFFSET):
                    return 0
                res = res * 10 + digit
                x = x // 10
            else:
                # 取负数，比如 -17 % 10 得到 3，-10 得到 -7，方便计算
                digit = 0 if x % 10 == 0 else x % 10 - 10
                # MIN % 10 代表 MIN // 10 小于 MIN * 10 多少
                # 负数的整数除法会向下取整，比如 -17 // 10 得到 -2
                if res < MIN_BOUND or (res == MIN_BOUND and digit < MIN_BOUND_OFFSET):
                    return 0
                res = res * 10 + digit
                # 负数要取整需要对齐到 10 的整数倍，否则向下取整，得不到十位上的结果
                x = (x - digit) // 10
        return res