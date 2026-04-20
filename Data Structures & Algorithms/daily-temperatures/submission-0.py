class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index] 
        #goal: maintain monotonic decreasing stack

        for i, t in enumerate(temperatures):
            #check if the temperature of head of stack is hotter
            # if true we can pop from stack
            while stack and stack[-1][0] < t: 
                stackT, stackI = stack.pop()
                res[stackI] = abs(stackI - i)
            stack.append([t, i])
        return res
