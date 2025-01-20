
class Solution:
    letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        res = list()
        # for i, c in enumerate(digits):
        #     index = ord(c) - ord('2')
        #     further = self.letterCombinations(digits[i + 1:])
        #     res
        if digits == "":
            return res
        index = ord(digits[0]) - ord("2")
        if len(digits) == 1:
            return [c for c in self.letters[index]]
        further = self.letterCombinations(digits[1:])
        for c in self.letters[index]:
            res += [c + s for s in further]
        return res