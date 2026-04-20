class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in hashmap:
                stack.append(c)
                continue
            if not stack or stack[-1] != hashmap[c]:
                return False
            stack.pop()
        return len(stack) == 0