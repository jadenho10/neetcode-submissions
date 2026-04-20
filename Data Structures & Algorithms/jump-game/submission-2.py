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
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0