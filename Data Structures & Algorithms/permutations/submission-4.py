class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = [] # all possible cases
        def dfs():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    dfs()
                    perms.pop()
        dfs()
        return res