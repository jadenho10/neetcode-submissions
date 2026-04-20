class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal, minVal = nums[0], nums[0]
        res = maxVal
        for i in range(1, len(nums)):
            num = nums[i]
            tempMax = max(num, maxVal * num, minVal * num)
            minVal = min(num, minVal * num, maxVal * num)

            maxVal = tempMax
            res = max(maxVal, res)
        
        return res