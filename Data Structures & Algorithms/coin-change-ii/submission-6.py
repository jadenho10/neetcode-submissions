'''
think recursive. why? we want to find all combinations that sum to this val

two choices at each step:
    @ index i we can either:
    add this number to our total count rn
    or skip this idx and go to i + 1

base case: total == amount, return 1
if total > amount or i > len(coins) return 0
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # (i, total) : count
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return memo[(i, total)]
        return dfs(0, 0)