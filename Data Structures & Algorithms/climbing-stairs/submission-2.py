class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        
        num1, num2 = 1, 2
        for i in range(3, n + 1):
            newNum2 = num1 + num2
            num1 = num2
            num2 = newNum2
        
        return num2