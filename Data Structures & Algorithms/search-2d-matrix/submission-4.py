class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        start, end = 0, (r * c) - 1
        while start <= end:
            mid = start + (end - start) // 2
            rows = mid // c
            cols = mid % c

            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False