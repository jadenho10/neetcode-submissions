class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} 
        def dfs(i: int, buying: bool):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            # cooldown := do nothing at this index
            cooldown = dfs(i + 1, buying)
            # we want to buy this coin rn
            if buying:
                # have to subtract e.g. 5 - 3 and 3 < 0 and dfs(i + 1, buying) = 5
                buy = dfs(i + 1, not buying) - prices[i] 
                maxVal = max(buy, cooldown)
            # we are selling this coin
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                maxVal = max(sell, cooldown)
            memo[(i, buying)] = maxVal
            return maxVal
        return dfs(0, True)

            