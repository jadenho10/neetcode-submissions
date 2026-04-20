class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        stack = [] # (index, heights)

        # maintain increasing order stack
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                index, hei = stack.pop()
                res = max(res, hei * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
