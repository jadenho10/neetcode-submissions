class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        inductionSum = (len(nums) * (len(nums) + 1)) // 2
        curSum = sum(nums)
        res = inductionSum - curSum
        return res