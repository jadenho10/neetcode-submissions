class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt = [-1] * (amount + 1) 

        def helper(amount):
            if amount == 0:
                return 0
            if opt[amount] != -1:
                return opt[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, helper(amount - coin) + 1)
                    
            opt[amount] = res
            return res
        total = helper(amount)
        return -1 if total == float('inf') else total

        # def coinRec(amount):
        #     if amount == 0:
        #         return 0
        #     res = float('inf')
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + coinRec(amount - coin))
        #     return res
        
        # return -1 if coinRec(amount) == float('inf') else coinRec(amount)


        