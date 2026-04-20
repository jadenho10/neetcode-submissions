class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (abs(j - i) <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res
