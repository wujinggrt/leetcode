from typing import Tuple

class Solution:

    def rounding(self, base: int, n: int, positive: bool) -> Tuple[bool, int]:
        if positive:
            MAX = 2**31 - 1
            MAX_BOUND = MAX // 10
            MAX_BOUND_OFFSET= MAX % 10
            if base > MAX_BOUND or (base == MAX_BOUND and n > MAX_BOUND_OFFSET):
                return True, MAX
        else:
            n = -n
            MIN = -2**31
            MIN_BOUND_OFFSET= 0 if (MIN % 10 == 0) else (MIN % 10 - 10)
            MIN_BOUND = (MIN - MIN_BOUND_OFFSET) // 10
            if base < MIN_BOUND or (base == MIN_BOUND and n < MIN_BOUND_OFFSET):
                return True, MIN
        res = base * 10 + n
        return False, res

    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        leadingWhitespace = True
        sign = 0 # for multiplication
        leadingZero = True
        num = 0
        digits = [n for n in range(ord('0'), ord('9') + 1)]
        for i, c in enumerate(s):
            if c == ' ' and leadingWhitespace:
                continue
            else:
                leadingWhitespace = False
            if c in ['+', '-']:
                if sign != 0: # duplicated
                    break
                sign = 1 if c == '+' else -1
            elif ord(c) in digits:
                if sign == 0:
                    sign = 1
                if leadingZero:
                    if int(c) == 0:
                        continue
                    else:
                        leadingZero = False
                rounded, num = self.rounding(num, int(c), sign > 0)
                if rounded:
                    break
            else:
                break
        return num