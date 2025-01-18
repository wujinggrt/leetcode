from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        long, short = nums1, nums2
        if len(long) < len(short):
            long, short = short, long
        # 从较长的list中，和较短的，两者不断调整。
        # 较长者确定一个下标 i，右侧都是
        lower_count = (len(short) + len(long) + 1) // 2
        left = 0
        right = len(short)
        while left < right:
            mid = left + (right - left) // 2
            long_count = lower_count - mid
            if short[mid] < long[long_count - 1]:
                # 需要mid处
                left = mid + 1
            else:
                right = mid
        # 现在确定了lower_count的区间在short[0,left-1],long[0,long_count-1]
        # 仅需确定总共数字个数奇偶，如果是奇数，那么中间值是lower_count区间最大值
        # 如果是偶数，中间值是lower_count区间最大值加上下一个最大值（从short和long下一个元素确定）
        INF = 1e6 + 1
        shorter_left_max = short[left - 1] if left != 0 else -INF
        longer_count = lower_count - left
        longer_left_max = long[longer_count - 1] if longer_count != 0 else -INF
        res1 = max(shorter_left_max, longer_left_max)
        if (len(long) + len(short)) % 2 == 1:
            return float(res1)
        res2 = min(
            short[left] if left != len(short) else INF,
            long[longer_count] if longer_count != len(long) else INF,
        )
        return (res1 + res2) / 2
