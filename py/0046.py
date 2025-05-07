import copy

class Solution:
    def dfs(self, res: List[List[int]], nums: List[int], track: List[int], visited: List[int]):
        if len(track) == len(nums):
            res.append(copy.deepcopy(track))
            return
        for i, num in enumerate(nums):
            if visited[i] == True:
                continue
            visited[i] = True
            track.append(num)
            self.dfs(res, nums, track, visited)
            track.pop()
            visited[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        visited = [False for _ in range(n)]
        track = list()
        self.dfs(res, nums, track, visited)
        return res