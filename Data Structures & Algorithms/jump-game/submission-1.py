"""
Brute force solution:
Recursion since we can use decision trees

- recursion(i = 0)
 - if i == last index return True
 - find the bound of the last element this index's element can reach
    - end = min(i + nums[i], last index)
- for j in (i + 1, j + 1):
- check if dfs(j) is True, return True if true

return False otherwise
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i): #index
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return True
            end = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
