class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        # find first no less than target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        span_left = left
        left, right = 0, len(nums)
        # find first greater than target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        span_right = left
        if span_left == span_right:
            return -1, -1
        return span_left, span_right - 1
