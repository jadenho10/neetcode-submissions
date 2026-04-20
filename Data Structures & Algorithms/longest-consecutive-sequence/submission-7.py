'''
constraints: 
nums is in range [-10^9, 10^9]
length of nums is 0, 1000

use a set(), we need to find numbers in the list FAST
hashsets make it so we can access num and num + 1

'''

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
            res = max(count, res)
        return res
        