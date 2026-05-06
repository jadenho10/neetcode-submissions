class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        memo = {}
        def dfs(r, c):
            if r == n:
                return m - c
            if c == m:
                return n - r
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            if word1[r] == word2[c]:
                memo[(r, c)] = dfs(r + 1, c + 1)
            else: # we can either insert, delete, replace
                memo[(r, c)] = 1 + min(dfs(r + 1, c), dfs(r + 1, c + 1), dfs(r, c + 1))
            return memo[(r, c)]
        return dfs(0, 0)

        