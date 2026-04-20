class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            ways = helper(i + 1)
            if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    ways += helper(i + 2)
            return ways

        return helper(0)