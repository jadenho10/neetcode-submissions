class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            # base case: represents how many insertions needed left
            if i == m:
                return n - j 
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            if (i, j) in dp:
                return dp[(i, j)]
            res = min(dfs(i + 1, j + 1), dfs(i, j + 1), dfs(i + 1, j))
            dp[(i, j)] = 1 + res
            return dp[(i, j)]
        return dfs(0, 0)

            