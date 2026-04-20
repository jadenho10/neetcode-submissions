from heapq import heappush, heappop, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)

    # return the kth largest int
    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]