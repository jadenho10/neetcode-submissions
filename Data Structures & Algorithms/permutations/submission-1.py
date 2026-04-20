class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return 
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs(i + 1)
                    subset.pop()
        dfs(0)
        return res