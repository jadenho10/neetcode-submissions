class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res
        
        slow, fast = n, helper(n)
        while fast != 1 and fast != slow:
            slow, fast = helper(slow), helper(helper(fast)) 
        return fast == 1
        