class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i, j, k):
            if (i, j) in dp:
                return dp[(i, j)]
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    dp[(i, j)] = True
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    dp[(i, j)] = True
                    return True
            dp[(i, j)] = False
            return False
        return dfs(0, 0, 0)