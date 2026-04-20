class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            elif s == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(s))

        return stack[0] 