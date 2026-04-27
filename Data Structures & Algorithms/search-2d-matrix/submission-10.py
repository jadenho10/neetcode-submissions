class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        total = ROWS * COLS

        l, r = 0, total - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        return False
