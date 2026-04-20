class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n)
        
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            end = min(i + nums[i], n - 1)
            for j in range(i + 1, end + 1):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]