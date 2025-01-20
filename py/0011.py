class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 思路：使用双指针，每次将对应数字较小的指针朝着另一个指针方向移动
        # 详解：双指针代表范围，指针分别指向的数为 x y，假设 x <= y，指针距离 t，容器容量为
        # min(x,y) * t = x * t，左指针不变，无论右指针向左移动多少，就算y变得再大，短板效应使得容量也不超过 x*t
        # 左指针向右移动，指向的数为 y1，此时两指针距离 t1，显然 t1 < t，并且 min(x,y1) <= min(x,y)
        # 具体地，y1<=y，min(x,y1)<=min(x,y)，此时容量最大情况为 x*t；如果 y1>y, min(x,y1)=x=min(x,y)
        # 有 min(x,yt)*t1<min(x,y)*t，所以，当 x 较小时，移动较大的指针不能找到容量更大的地方。
        # 所以，我们需要移动较小的指针。
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(area, res)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res