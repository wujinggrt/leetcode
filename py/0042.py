from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         monotonic_stack: List = list()
#         water: int = 0
#         for i in range(len(height)):
#             while len(monotonic_stack) != 0 and height[i] > height[monotonic_stack[-1]]:
#                 hole = monotonic_stack.pop()
#                 if len(monotonic_stack) == 0:  # corner case：最后一块
#                     break
#                 left = monotonic_stack[-1]
#                 width = i - left - 1
#                 deep = min(height[left], height[i]) - height[hole]
#                 water += deep * width
#             monotonic_stack.append(i)
#         return water

class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped = 0
        while i < j:
            left_max = max(height[i], left_max)
            right_max = max(height[j], right_max)
            if height[i] < height[j]:
                trapped += left_max - height[i]
                i += 1
            else:
                trapped += right_max - height[j]
                j -= 1
        return trapped