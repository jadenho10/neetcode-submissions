class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prevEnd:
                prevEnd = e
            else:
                count += 1
                prevEnd = min(e, prevEnd)
        return count