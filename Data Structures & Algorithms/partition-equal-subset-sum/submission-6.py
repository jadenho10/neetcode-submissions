class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        #goal: get sum to sum(nums) / 2
        dp = {}
        def dfs(i, curr):
            if curr == sum(nums) // 2:
                return True
            if i >= len(nums) or curr > sum(nums) // 2:
                return False
            if (i, curr) in dp:
                return dp[(i, curr)]
            dp[(i, curr)] = dfs(i + 1, curr) or dfs(i + 1, curr + nums[i])
            return dp[(i, curr)]
        return dfs(0, 0)