class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins) or curr > amount:
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            memo[(i, curr)] = dfs(i + 1, curr) + dfs(i, curr + coins[i])
            return memo[(i, curr)]
        return dfs(0, 0)

