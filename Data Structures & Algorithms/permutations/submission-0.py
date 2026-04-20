class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        permute = []
        def dfs():
            if len(permute) == len(nums):
                res.append(permute.copy())
                return
            
            for num in nums:
                if num not in permute:
                    permute.append(num)
                    dfs()
                    permute.pop()
            
        dfs()
        return res
