class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs", 
            "8" : "tuv", 
            "9" : "wxyz"
        }

        def dfs(i: int, substr: str):
            if len(substr) == len(digits):
                res.append(substr)
                return
            for c in hashmap[digits[i]]:
                dfs(i + 1, substr + c)
        if digits:
            dfs(0, "")
        return res