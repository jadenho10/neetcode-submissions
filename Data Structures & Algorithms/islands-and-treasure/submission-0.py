class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    r < 0
                    or c < 0
                    or r >= ROWS
                    or c >= COLS
                    or grid[r][c] != INF
                ):
                    continue
                q.append([r, c])
                grid[r][c] = grid[row][col] + 1
