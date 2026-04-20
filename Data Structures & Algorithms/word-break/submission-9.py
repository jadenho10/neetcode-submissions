class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)
        def dfs(i):
            if i == len(s):
                return True
            if dp[i] is not None:
                return dp[i]
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    if dfs(i + len(w)):
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]
        return dfs(0)