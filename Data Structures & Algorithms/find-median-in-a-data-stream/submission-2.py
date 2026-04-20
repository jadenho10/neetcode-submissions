from heapq import heappush, heappop, heapify
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)
        


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0] 
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        