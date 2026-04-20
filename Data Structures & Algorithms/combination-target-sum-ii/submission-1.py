class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(total, array, i):
            if total == target:
                res.append(array.copy())
                return
            elif i > len(nums) - 1 or target < total:
                return 
            array.append(nums[i])
            dfs(total + nums[i], array, i + 1)
            array.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(total, array, i + 1)
        dfs(0, [], 0)
        return res