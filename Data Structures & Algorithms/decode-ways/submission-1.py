class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        def helper(i):
            if i == n:
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0
            
            ways = helper(i + 1)
            if (i < len(s) - 1 and 
                (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'))):
                    ways += helper(i + 2)
            dp[i] = ways
            return ways

        return helper(0)