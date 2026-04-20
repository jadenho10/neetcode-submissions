class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet: 
            if (num - 1) in numSet:
                continue
            count = 1
            while (num + count) in numSet:
                count += 1
            res = max(res, count)
        return res 
