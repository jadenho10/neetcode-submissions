'''
2d dp problem
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # edge case: lengths of s1, s2 dont equal s3
        n, m, z = len(s1), len(s2), len(s3)
        if n + m != z: 
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                # decision tree
                if i < n and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                elif j < m and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]