class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[r]:
                l += 1
            else:
                r -= 1
            
        minimum = min(minimum, nums[l])  
        return minimum 