class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, bought):
            if i >= len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            cooldown = dfs(i + 1, bought)

            if bought:
                buy = dfs(i + 1, not bought) - prices[i]
                dp[(i, bought)] = max(buy, cooldown) 
            else:
                sell = dfs(i + 2, not bought) + prices[i]
                dp[(i, bought)] = max(sell, cooldown) 
            return dp[(i, bought)]
        return dfs(0, True)
        