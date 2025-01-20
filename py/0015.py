class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = list()
        for i, n in enumerate(nums):
            if n > 0:
                # 后面的全部大于 0
                break
            if i != 0 and n == nums[i - 1]:
                # avoid duplicate
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp = n + nums[j] + nums[k]
                if tmp == 0:
                    res.append([n, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        # 避免重复添加结果
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    k -= 1
        return res