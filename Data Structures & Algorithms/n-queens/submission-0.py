class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet, posDiag, negDiag = set(), set(), set()
        # cols, (r + c), (r - c)
        res = []
        board = [["."] * n for _ in range(n)]
        
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            # go through each column and see if you can place your queen
            for c in range(n):
                if c in colSet or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                colSet.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)

                colSet.discard(c)
                posDiag.discard(r + c)
                negDiag.discard(r - c)
                board[r][c] = "."
        dfs(0)
        return res

