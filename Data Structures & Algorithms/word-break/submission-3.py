class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo = {len(s) : True}
        # def helper(n):
        #     if n in memo:
        #         return memo[n]
        #     for w in wordDict:
        #         if (n + len(w)) <= len(s) and s[n: n + len(w)] == w:
        #             if helper(n + len(w)):
        #                 memo[n] = True
        #                 return True
        #     memo[n] = False
        #     return False

        # return helper(0) 

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)] 
                if dp[i]:
                    break
        return dp[0]
