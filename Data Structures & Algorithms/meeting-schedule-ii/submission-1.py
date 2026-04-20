"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        res, count = 0, 0
        
        st, en = 0, 0
        while st < len(intervals):
            if start[st] < end[en]:
                st += 1
                count += 1
            else:
                en += 1
                count -= 1
            res = max(res, count)
        return res 

        
            
        