class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        dp = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        def dfs(i, curr):
            if curr == target:
                return True
            if i == len(nums) or curr > target:
                return False
            if dp[i][curr] is not None:
                return dp[i][curr]
            dp[i][curr] = dfs(i + 1, curr) or dfs(i + 1, curr + nums[i])
            return dp[i][curr]

        return dfs(0, 0)