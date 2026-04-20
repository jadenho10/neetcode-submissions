class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, array, total):
            if total == target:
                res.append(array.copy())
                return
            elif index > len(nums) - 1 or total > target:
                return 
            
            array.append(nums[index])
            dfs(index, array, total + nums[index])
            array.pop()
            dfs(index + 1, array, total)

        dfs(0, [], 0)
        return res