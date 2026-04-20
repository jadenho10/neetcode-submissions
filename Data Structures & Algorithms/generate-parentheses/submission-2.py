class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(substr):
            if len(substr) == 2 * n:
                if self.valid(substr):
                    res.append(substr)
                return 
            dfs(substr + "(")
            dfs(substr + ")")
        dfs("")
        return res
        
        
    def valid(self, string):
        opened, closed = 0, 0
        for c in string:
            if c == "(":
                opened += 1
            else:
                closed += 1
            if closed > opened:
                return False
        return opened == closed