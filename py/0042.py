from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        monotonic_stack: List = list()
        water: int = 0
        for i in range(len(height)):
            while len(monotonic_stack) != 0 and height[i] > height[monotonic_stack[-1]]:
                hole = monotonic_stack.pop()
                if len(monotonic_stack) == 0:  # corner case：最后一块
                    break
                left = monotonic_stack[-1]
                width = i - left - 1
                deep = min(height[left], height[i]) - height[hole]
                water += deep * width
            monotonic_stack.append(i)
        return water

