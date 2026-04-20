'''
start
Example: 
[1, 2, 3] 

Decision Tree
    base case: i = 1, i = 2 return 0
    otherwise: opt() := recursive relation
    opt(i) = min(opt(i - 2) + nums[i - 2], opt(i - 1) + nums[i - 1])

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]
