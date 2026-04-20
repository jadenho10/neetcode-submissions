class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        return (self.nums[n // 2] if (n & 1) else
                (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2)
        