class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c, lastHeight):
            if (r == ROWS or c == COLS or r < 0 or c < 0
                or matrix[r][c] <= lastHeight):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        res = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
                
        return res