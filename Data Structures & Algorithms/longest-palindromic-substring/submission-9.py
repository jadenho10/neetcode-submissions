class Solution:
    def longestPalindrome(self, s: str) -> str:
        index, length = 0, 0
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)] 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (abs(j - i) <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > length:
                        length = j - i + 1
                        index = i

        return s[index:index + length]