class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
                else:
                    continue
       
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r < 0
                        or c < 0
                        or r == ROWS
                        or c == COLS
                        or grid[r][c] != 1
                        ):
                            continue
                    q.append([r, c])
                    grid[r][c] = 2 
                    fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1



