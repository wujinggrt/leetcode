from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif nums[left] > mid_num:
                # [left:mid] 有两个递增区间, [mid:right] 有一个递增区间
                if mid_num <= target and target < nums[left]:
                    # 单个区间情况会轻松。注意，需要 + 1
                    left = mid + 1
                else:
                    right = mid
            elif mid_num > nums[right - 1]:
                # [left:mid] 递增，[mid:right] 有两个递增区间
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                # sorted, and find the lower_bound
                if mid_num < target:
                    left = mid + 1
                else:
                    right = mid
        return left if left != len(nums) and nums[left] == target else -1
