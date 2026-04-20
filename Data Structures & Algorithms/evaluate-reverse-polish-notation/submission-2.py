class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())

            elif s == "*":
                stack.append(stack.pop() * stack.pop())

            elif s == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            elif s == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a-b)
            else: 
                stack.append(int(s)) 
        return stack[0]       