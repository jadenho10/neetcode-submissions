'''
asteroids[i] != 0

maintain a stack: [], maybe only add positive asteroids 

note: to tell if top of stack is pos/neg, ill use a bool var: isNeg

if stack is empty or we have that this asteroid has the same sign as the top of stack, 
push into stack:
    if not stack or (isNeg and A[i] < 0) or (!isNeg and A[i]>0): push into stack

    else:
        winner = 0
        if abs(stack.pop()) < abs(A[i]) : push A[i]
        else if abs(stack.pop()) > abs(A[i]) 
        else: continue
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
                
        return stack
        
        