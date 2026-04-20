class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals:
            lastEnd = res[-1][1]
            if interval[0] <= lastEnd: 
                lastEnd = max(lastEnd, interval[1])
                res[-1][1] = lastEnd
            else:
                res.append(interval)
        return res
