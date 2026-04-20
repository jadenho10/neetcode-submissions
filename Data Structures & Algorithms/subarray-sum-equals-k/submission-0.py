class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0 : 1} # curSum : occurences while traversing arr
        curSum = 0

        res = 0
        for i, num in enumerate(nums):
            curSum += num
            diff = curSum - k
            res += counts.get(diff, 0)
            counts[curSum] = 1 + counts.get(curSum, 0)
        return res
            