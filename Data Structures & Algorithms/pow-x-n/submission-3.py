class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        if n < 0:
            n = -1.0 * n
            x = 1.0 / x
        res = 1
        while n > 0:
            if n % 2:
                res *= x
                n -= 1
            x *= x
            n //= 2
        return res