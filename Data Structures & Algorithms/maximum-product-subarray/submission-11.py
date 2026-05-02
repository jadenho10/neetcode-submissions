class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = minVal = nums[0]
        res = maxVal
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, maxVal * curr, minVal * curr)

            minVal = min(curr, minVal * curr, maxVal * curr)
            maxVal = tempMax
            res = max(res, maxVal)
        return res