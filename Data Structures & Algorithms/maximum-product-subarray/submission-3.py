class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = nums[0], nums[0]
        res = curMax

        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, curMax * curr, curMin * curr)
            curMin = min(curr, curMax * curr, curMin * curr)

            curMax = tempMax
            res = max(res, curMax)
        return res