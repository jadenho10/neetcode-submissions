class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        minIndex = l

        if minIndex == 0:
            l, r = 0, len(nums) - 1
        elif nums[minIndex] <= target and target <= nums[-1]:
            l, r = minIndex, len(nums) - 1
        else:
            l, r = 0, minIndex - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        