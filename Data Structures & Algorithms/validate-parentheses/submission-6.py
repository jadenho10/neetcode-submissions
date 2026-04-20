class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', ']' : '[', '}' : '{'} 

        for c in s:
            if c not in hashmap:
                stack.append(c)
            elif not stack or hashmap[c] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack