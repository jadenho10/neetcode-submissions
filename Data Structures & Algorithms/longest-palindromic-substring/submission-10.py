class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        idx, length = 0, 0
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > length:
                        idx = i
                        length = j - i + 1
        
        return s[idx : idx + length]

