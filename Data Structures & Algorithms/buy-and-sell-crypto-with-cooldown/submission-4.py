class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        # buying : True
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                maxVal = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                maxVal = max(sell, cooldown)

            memo[(i, buying)] = maxVal
            return maxVal
        
        return dfs(0, True)