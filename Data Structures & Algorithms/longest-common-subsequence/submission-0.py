class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = [[-1] * (m) for i in range(n)] 
        def opt(i, j): # we will start with (0, 0)
            if i == n or j == m:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i] == text2[j]:
                memo[i][j] = 1 + opt(i + 1, j + 1)
                return memo[i][j]

            memo[i][j] =  max(opt(i + 1, j), opt(i, j + 1))
            return memo[i][j]
        return opt(0, 0)