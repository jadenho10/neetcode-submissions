class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def helper(nums, prev, index): #index will start at 0
            if index == len(nums):
                return 0
            exclude = helper(nums, prev, index + 1)
            include = 0
            if nums[index] > prev:
                include = 1 + helper(nums, nums[index], index + 1)
            return max(include, exclude)

        return helper(nums, float('-inf'), 0)