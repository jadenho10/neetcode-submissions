class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jumps = 0

        while r < len(nums) - 1:
            maxDist = 0
            for i in range(l, r + 1):
                maxDist = max(maxDist, nums[i] + i)
            jumps += 1
            l = r + 1
            r = maxDist
        return jumps