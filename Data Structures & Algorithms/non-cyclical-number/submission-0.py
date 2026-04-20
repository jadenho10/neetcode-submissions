class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(n: int) -> int:
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res
        slow, fast = n, nextNum(n)

        while fast != 1 and slow != fast:
            slow, fast = nextNum(slow), nextNum(nextNum(fast))
        return fast == 1