from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        i, res = 0, {}

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # eliminate intervals s.t. interval is too far to the left from query
            while minHeap and minHeap[0][1] < q:
                heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
