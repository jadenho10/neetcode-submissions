class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subarr = []

        def dfs(i, total):
            if i == len(candidates) and total == target:
                res.append(subarr.copy())
                return
            elif i == len(candidates) or total > target:
                return
            
            subarr.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subarr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res