class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        INF = 2147483647

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        while q:
            nr, nc = q.popleft()
            for dr, dc in DIRECTIONS:
                r, c = nr + dr, nc + dc
                if (r < 0 or c < 0 or r == ROWS or c == COLS
                    or grid[r][c] != INF):
                    continue
                grid[r][c] = 1 + grid[nr][nc]
                q.append([r, c])
        
