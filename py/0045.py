class Solution:
    def jump(self, nums: List[int]) -> int:
        boarder = 0
        max_position = 0
        num_jump = 0
        i = 0
        for i, num in enumerate(nums):
            if boarder >= len(nums) - 1:
                break
            max_position = max(max_position, i + num)
            if i == boarder:
                # Reached the boarder
                boarder = max_position
                num_jump += 1
        return num_jump