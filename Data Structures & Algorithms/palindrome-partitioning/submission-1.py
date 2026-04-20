class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isValid(valid_str):
            l, r = 0, len(valid_str) - 1
            while l < r:
                if valid_str[l] != valid_str[r]:
                    return False
                l += 1
                r -= 1
            return True

        subset = []
        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                if isValid(s[i:j + 1]):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()
        dfs(0)
        return res
