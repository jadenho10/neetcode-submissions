class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s):
            closed, opened = 0, 0
            for c in s:
                if c == "(":
                    opened += 1
                else:
                    closed += 1
                if closed > opened:
                    return False
            return closed == opened

        res = []
        def dfs(substr):
            if len(substr) == 2 * n:
                if valid(substr):
                    res.append(substr)
                return 
            dfs(substr + "(")
            dfs(substr + ")")
        dfs("")
        return res