class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]]

        visit.add((0, 0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    row < 0 
                    or col < 0
                    or row == N
                    or col == N
                    or (row, col) in visit
                ):
                    continue
                visit.add((row, col))
                heapq.heappush(minHeap, [max(t, grid[row][col]), row, col])