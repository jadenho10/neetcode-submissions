class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checkpoint = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= checkpoint:
                checkpoint = i
        return checkpoint == 0 