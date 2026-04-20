class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def helper(n):
            if n in memo:
                return memo[n]
            for w in wordDict:
                if (n + len(w)) <= len(s) and s[n: n + len(w)] == w:
                    if helper(n + len(w)):
                        memo[n] = True
                        return True
            memo[n] = False
            return False

        return helper(0) 
