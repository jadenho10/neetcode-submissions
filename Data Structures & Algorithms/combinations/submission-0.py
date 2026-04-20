class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i):
            if len(comb) == k:
                res.append(comb.copy())
                return 
            if i > n:
                return
            comb.append(i)
            dfs(i + 1)
            comb.pop()
            dfs(i + 1)

        
        dfs(1)
        return res