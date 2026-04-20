class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start, end = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < end:
                res += 1
                end = min(end, currEnd)
            else:
                end = currEnd
        return res