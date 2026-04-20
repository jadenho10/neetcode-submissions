class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # you now know that l = r = ** min val index **
        minI = l
        
        if not minI:
            l, r = 0, len(nums) - 1
        elif nums[minI] <= target <= nums[-1]:
            l, r = minI, len(nums) - 1
        else:
            l, r = 0, minI - 1
            
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
