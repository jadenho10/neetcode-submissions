class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # monotonic decreasing pair (idx, t)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackIdx, stkTmp = stack.pop()
                res[stackIdx] = i - stackIdx 
            stack.append([i, t])
        return res


