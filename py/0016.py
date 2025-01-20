class Solution:
    def abs(self, n: int) -> int:
        return n if n >= 0 else -n

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 2**31 - 1
        i = 0
        while i < len(nums) - 2:
            n = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                minSum = sum(nums[i : i + 3])
                maxSum = n + nums[k] + nums[k - 1]
                tmp = n + nums[j] + nums[k]
                # 边界情况检查
                if self.abs(minSum - target) < self.abs(res - target):
                    res = minSum
                if self.abs(maxSum - target) < self.abs(res - target):
                    res = maxSum
                if self.abs(tmp - target) < self.abs(res - target):
                    res = tmp
                if target < minSum or target > maxSum:
                    break
                if target in [minSum, maxSum, tmp]:
                    return target
                if tmp > target:
                    # 优化，跳过相同元素
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                # 跳过 i 处的重复元素
                i += 1
            i += 1
        return res