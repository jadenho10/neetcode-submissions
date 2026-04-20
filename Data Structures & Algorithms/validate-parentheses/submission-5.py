class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']':'['}
        for c in s:
            # opening
            if c not in hashmap:
                stack.append(c)
            elif not stack or stack[-1] != hashmap[c]:
                return False
            else:
                stack.pop()
        return not len(stack)

