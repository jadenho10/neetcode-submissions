class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(total, array, index) -> None:
            if total == target:
                res.append(array.copy())
                return 
            elif total > target or index > len(nums) - 1:
                return
            
            array.append(nums[index])
            dfs(total + nums[index], array, index)
            array.pop()
            dfs(total, array, index + 1)
        dfs(0, [], 0)
        return res