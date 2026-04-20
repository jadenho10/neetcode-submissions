class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def opt(i, j):
            if i == len(nums):
                return 0
            LIS = opt(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + opt(i + 1, i))
        
            return LIS

        return opt(0, -1)