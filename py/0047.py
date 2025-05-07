import copy

class Solution:

    def dfs(self, res: List[List[int]], nums: List[int], track: List[int], visited: List[bool]) -> None:
        if len(track) == len(nums):
            res.append(copy.deepcopy(track))
            return
        for i, num in enumerate(nums):
            if visited[i] or (i != 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            visited[i] = True
            track.append(num)
            self.dfs(res, nums, track, visited)
            track.pop()
            visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        track = list()
        visited = [False for _ in nums]
        self.dfs(res, nums, track, visited)
        return res