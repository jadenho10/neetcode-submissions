class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return 
            if total > target or i == len(nums):
                return 
            
            subset.append(nums[i])
            dfs(i + 1, total + nums[i])
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res
