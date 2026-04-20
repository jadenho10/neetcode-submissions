class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]




        # def helper(nums, n):
        #     if n < 0:
        #         return 0
        #     return max(helper(nums, n - 2) + nums[n], helper(nums, n - 2))

        # return helper(nums, len(nums) - 1)
        