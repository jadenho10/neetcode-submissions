class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        # s, t
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return dp[(i, j)]
            

        return dfs(0, 0)