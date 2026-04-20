class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        numbers = set(nums)
        for n in numbers:
            if n - 1 not in numbers:
                current = 1
                while n + current in numbers:
                    current += 1
            longest = max(current, longest)

        return longest
            

        