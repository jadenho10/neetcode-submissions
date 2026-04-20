'''
Decision Tree:
(i in [0, len(P)], bought = True or False)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            # two cases: in the past, we alr purchased a coin or didnt
            cooldown = dfs(i + 1, buying)
            if buying: # we purchased a coin
                # choose to sell or skip day
                buy = dfs(i + 1, not buying) - prices[i]
                maxVal = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                maxVal = max(sell, cooldown) 
            memo[(i, buying)] = maxVal
            return memo[(i, buying)]
        return dfs(0, True)
            