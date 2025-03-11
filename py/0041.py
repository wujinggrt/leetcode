class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            nums[i] = num if num > 0 else (n + 1)
        for i, num in enumerate(nums):
            abs_num = abs(num)
            if abs_num > 0 and abs_num <= n:
                nums[abs_num - 1] = -abs(nums[abs_num - 1])
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1