class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set(nums)
        return len(dupSet) != len(nums)