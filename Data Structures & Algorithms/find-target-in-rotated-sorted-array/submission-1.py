class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l += 1
                else:
                    r -= 1
            else:
                if target < nums[mid] or target > nums[r]:
                    l += 1
                else:
                    r -= 1
        return -1