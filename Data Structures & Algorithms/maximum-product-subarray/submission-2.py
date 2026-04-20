class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1, 1 # neutral value

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(curMax, res)
        return res