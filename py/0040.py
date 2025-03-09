from copy import deepcopy
class Solution:

    def dfs(self, i: int, target: int):
        if target == 0:
            self.combinations.append(deepcopy(self.track))
            return
        previous = -1
        for j, num in enumerate(self.candidates[i+1:], start=i+1):
            if num > target:
                break
            # if previous != -1 and num == self.candidates[previous]:
            #     continue # duplicated
            previous = j
            self.track.append(num)
            self.dfs(j, target - num)
            self.track.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.candidates.sort()
        self.track = list()
        self.combinations = list()
        self.dfs(-1, target)
        return self.combinations
