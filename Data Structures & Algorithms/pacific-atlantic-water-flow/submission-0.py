class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacSet, atlSet = set(), set()
        res = [] # answer

        def dfs(r, c, visit, lastHeight):
            if (
                r < 0
                or c < 0
                or r >= len(heights)
                or c >= len(heights[0])
                or (r, c) in visit
                or heights[r][c] < lastHeight
                ):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for r in range(len(heights)):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, len(heights[0]) - 1, atlSet, heights[r][len(heights[0]) - 1])

        for c in range(len(heights[0])):
            dfs(0, c, pacSet, heights[0][c])
            dfs(len(heights) - 1, c, atlSet, heights[len(heights) - 1][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in atlSet and (r, c) in pacSet:
                    res.append((r, c))

        return res            
        
    