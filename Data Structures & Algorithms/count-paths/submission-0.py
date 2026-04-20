class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        opt = [[-1] * (n + 1) for i in range(m + 1)]
        def helper(m, n, opt): 
            if m == 1 or n == 1:
                return 1
            if opt[m][n] != -1:
                return opt[m][n]
            opt[m][n] = helper(m, n - 1, opt) + helper(m - 1, n, opt)
            return opt[m][n]
        return helper(m, n, opt)