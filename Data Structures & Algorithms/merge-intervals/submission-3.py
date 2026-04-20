class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = res[-1][1]
            start, end = intervals[i]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append(intervals[i])
        return res

