class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        indegree = [[0] * COLS for _ in range(ROWS)]
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                for row, col in directions:
                    nr, nc = row + r, col + c
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        matrix[nr][nc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    q.append([r, c])

        count = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row in range(ROWS) and col in range(COLS) 
                        and matrix[r][c] < matrix[row][col]):
                        indegree[row][col] -= 1
                        if indegree[row][col] == 0:
                            q.append([row, col])
            count += 1
        return count




        