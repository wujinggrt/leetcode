class Standing:
    def __init__(self):
        self.cols = list()
        self.index_diffs = list()
        self.index_sums = list()

    def insert_distinct(self, row: int, col: int) -> bool:
        if col in self.cols:
            return False
        index_diff = row - col
        if index_diff in self.index_diffs:
            return False
        index_sum = row + col
        if index_sum in self.index_sums:
            return False
        self.cols.append(col)
        self.index_diffs.append(index_diff)
        self.index_sums.append(index_sum)
        return True

    def remove(self, row: int, col: int) -> None:
        self.cols.remove(col)
        self.index_diffs.remove(row - col)
        self.index_sums.remove(row + col)


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        boards: list[list[str]] = list()
        peaceStandings: list[int] = [-1 for _ in range(n)]
        standing = Standing()
        self.backtrack(boards, peaceStandings, standing, 0)
        return boards

    def backtrack(
        self, boards: list[list[str]], peaceStandings: list[int], standing: Standing, row: int
    ) -> None:
        n = len(peaceStandings)
        if row == n:
            board = [["." if mark != i else "Q" for i in range(n)] for mark in peaceStandings]
            boards.append(["".join(line) for line in board])
            return
        for col in range(n):
            if not standing.insert_distinct(row, col):
                continue
            peaceStandings[row] = col
            self.backtrack(boards, peaceStandings, standing, row + 1)
            peaceStandings[row] = -1
            standing.remove(row, col)
