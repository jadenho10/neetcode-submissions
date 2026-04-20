class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i == ROWS
                or j == COLS
                or board[i][j] != "O"
            ):
                return
            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        #dfs unsurrounded ones
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] 
                    or c in [0, COLS - 1]):
                    dfs(r, c)

        #change remaining O's to T's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        #change "T" to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"