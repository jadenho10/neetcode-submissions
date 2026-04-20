"""
RETURN A STRING
USE 2D DP TABLE
From i from 0 to len(str)
  From j from i to len(str)
   Check if the string from i to j is a palindrome
      THIS IS WHERE THE DP RECURSIVE SEQUENCE COMES IN

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        index, length = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if length < (j - i + 1):
                        index = i
                        length = j - i + 1
        return s[index: index + length]