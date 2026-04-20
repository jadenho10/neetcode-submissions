class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlSet, pacSet = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, COLS - 1, atlSet, heights[r][COLS - 1]) 
        for c in range(COLS):
            dfs(0, c, pacSet, heights[0][c])
            dfs(ROWS - 1, c, atlSet, heights[ROWS - 1][c]) 

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlSet and (r, c) in pacSet:
                    res.append([r, c])
        return res
        