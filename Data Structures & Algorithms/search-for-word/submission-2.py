class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r,c) < 0 
            or r == len(board)
            or c == len(board[0])
            or (r, c) in visited
            or word[i] != board[r][c]    
            ):
                return False

            visited.add((r,c))
            res = (dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1))
            visited.remove((r,c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
