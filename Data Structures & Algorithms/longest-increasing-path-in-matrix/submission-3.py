class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, prevVal):

            if (
                i < 0
                or j < 0
                or i == ROWS
                or j == COLS
                or matrix[i][j] <= prevVal
            ):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))

            dp[(i, j)] = res
            return dp[(i, j)]
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j, -1))
        return res

