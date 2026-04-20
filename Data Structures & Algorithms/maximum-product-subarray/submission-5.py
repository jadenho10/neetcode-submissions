class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal, minVal = nums[0], nums[0]
        res = maxVal
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(maxVal * curr, minVal * curr, curr)
            minVal = min(minVal * curr, maxVal * curr, curr)

            maxVal = tempMax
            res = max(maxVal, res)
        return res
