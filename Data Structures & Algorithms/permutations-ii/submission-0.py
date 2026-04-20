class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        perms = []

        def dfs():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            for num in count:
                if count[num]:
                    perms.append(num)
                    count[num] -= 1
                    dfs()

                    count[num] += 1
                    perms.pop()
        dfs()
        return res