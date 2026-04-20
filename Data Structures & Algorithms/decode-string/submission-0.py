class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                word = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                stack.append(int(count) * word)
        return "".join(stack)