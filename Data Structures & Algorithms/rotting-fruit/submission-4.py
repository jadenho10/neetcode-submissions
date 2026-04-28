class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        either want to stop when we run out of fruit to rot
        i.e. no more adjacent fresh fruit next to rotten ones
        
        BFS
        """
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0 # need count of fresh so we know when to stop BFS

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        # if either one condition fails, end BFS
        res = 0 # total num of mins
        while q and fresh > 0:
            for _ in range(len(q)):
                nr, nc = q.popleft()
                for dr, dc in DIRECTIONS:
                    r, c = nr + dr, nc + dc
                    # stop if out of bounds or not a fresh fruit
                    if (r < 0 or c < 0 or r == ROWS or c == COLS
                        or grid[r][c] != 1):
                        continue

                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
            res += 1
        return res if fresh == 0 else -1




        