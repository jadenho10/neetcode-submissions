class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(" , "]":"[", "}":"{"}

        for c in s:
            if stack and c in hashmap and hashmap[c] == stack[-1]:
                stack.pop()
            elif c not in hashmap:
                stack.append(c)
            else:
                return False
        return not len(stack)
 