class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins) or curr > amount:
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            dp[(i, curr)] = dfs(i + 1, curr) + dfs(i, curr + coins[i])
            return dp[(i, curr)]
        return dfs(0, 0) 
            