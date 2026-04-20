class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums) # 0, 1, 2 

        R, W, B = counter[0], counter[1], counter[2]
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

