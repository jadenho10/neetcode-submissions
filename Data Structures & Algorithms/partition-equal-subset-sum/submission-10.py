class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        half = total // 2
        memo = {}
        def dfs(i, total):
            if total == half:
                return True
            if i == len(nums) or total > half:
                return False

            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return memo[(i, total)]
        return dfs(0, 0)
