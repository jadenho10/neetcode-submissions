class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(memo: List[int], val: List[int], i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return val[0]
            if memo[i] != -1:
                return memo[i]
            pick = val[i] + helper(memo, val, i - 2)
            skip = helper(memo, val, i - 1)
            memo[i] = max(pick, skip)
            return memo[i]
        
        n = len(nums)
        memo1 = [-1] * n
        memo2 = [-1] * n

        skipFirst = helper(memo1, nums[1:], n - 2)  # Fixed index
        skipLast = helper(memo2, nums[:n - 1], n - 2)  # Fixed index

        return max(skipFirst, skipLast)
