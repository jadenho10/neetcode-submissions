class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2: return False

        memo = {}
        def dfs(i, total):
            if total == target:
                return True
            
            # we couldnt reach target
            if i >= len(nums) or total > target:
                return False
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = dfs(i + 1, total) or dfs(i + 1, total + nums[i])
            return memo[(i, total)]

        return dfs(0, 0)            
