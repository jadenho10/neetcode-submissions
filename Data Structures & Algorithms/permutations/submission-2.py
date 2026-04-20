class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs()
                    subset.pop()
        dfs()
        return res
