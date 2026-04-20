from heapq import heappush, heappop, heapify
class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            maxVal = -1 * heappop(self.small)
            heappush(self.large, maxVal) 
        if len(self.large) > len(self.small) + 1:
            minVal = -1 * heappop(self.large)
            heappush(self.small, minVal) 

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + -1 * self.small[0]) / 2.0