class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visit or board[r][c] != word[index]):
                return False
            visit.add((r, c))
            verify = (dfs(r + 1, c, index + 1) or dfs(r, c + 1, index + 1) or
                dfs(r - 1, c, index + 1) or dfs(r, c - 1, index + 1))
            visit.remove((r, c))
            return verify
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
