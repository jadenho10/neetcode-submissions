class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        length = (row * col) - 1

        l, r = 0, length
        while l <= r:
            mid = l + (r - l) // 2
            i = mid // col
            j = mid % col
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False