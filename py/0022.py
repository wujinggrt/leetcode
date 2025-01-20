class Solution:
    def dfs(self, res: List[str], p: List[str], left: int, right: int, n: int):
        if len(p) == 2 * n:
            res.append("".join(p))
            return
        if left < n:
            p.append("(")
            self.dfs(res, p, left + 1, right, n)
            p.pop()
        if right < left:
            p.append(")")
            self.dfs(res, p, left, right + 1, n)
            p.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        # 复杂度参考卡特蓝书C 2n n  1 / (n + 1)
        res = list()
        p = list()
        self.dfs(res, p, 0, 0, n)
        return res