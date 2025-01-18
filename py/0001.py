from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value 是索引，key 是 value 索引着的数字距离 target 的差
        # 所以只需要将数字作为 key，便可查找是否存在恰好以此数字作为与target的差
        # 存在即答案。
        gap_index = {target - nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            if nums[i] in gap_index:
                ans = gap_index[nums[i]]
                if i != ans:
                    return sorted(list([i, gap_index[nums[i]]]))
        raise ValueError("No two sum solution")


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
