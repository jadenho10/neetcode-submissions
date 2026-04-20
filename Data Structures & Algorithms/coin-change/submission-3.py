class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1) # dp table to map min coins at each value
        dp[0] = 0
        for a in range(1, (amount + 1)):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a - c], dp[a])
        return dp[amount] if dp[amount] != float('inf') else -1
