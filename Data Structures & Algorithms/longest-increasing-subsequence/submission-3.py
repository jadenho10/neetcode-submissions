class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])
        return max(dp)