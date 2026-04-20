class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt - c] + 1, dp[amt])
        return dp[amount] if dp[amount] != float('inf') else -1

        # def coinRec(amount):
        #     if amount == 0:
        #         return 0
        #     res = float('inf')
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + coinRec(amount - coin))
        #     return res
        
        # return -1 if coinRec(amount) == float('inf') else coinRec(amount)


        