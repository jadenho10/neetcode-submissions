class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removeIndices = set()
        stack = [] # add index
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            else:
                if not stack:
                    removeIndices.add(i)
                else:
                    stack.pop()

        removeIndices = removeIndices.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in removeIndices:
                res.append(c)
        return "".join(res)