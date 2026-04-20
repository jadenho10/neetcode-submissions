class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        totalTime = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    queue.append((r,c))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row >= 0 
                    and col >= 0 
                    and row < ROWS
                    and col < COLS 
                    and grid[row][col] == 1):
                        queue.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            totalTime += 1
        if fresh == 0:
            return totalTime
        else:
            return -1