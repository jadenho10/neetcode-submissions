"""
wanna change word1 to word2:
find the min num of operations

base case:
dfs(i, j)  # m = len(word1), len(word2)
if i == m; return n - j
if j == n; return m - i

if word1[i] == word2[j]: dfs(i, j) = dfs(i + 1, j + 1)
else dfs(i, j) = 1 + min (dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

dfs(0, 0)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)
            
        