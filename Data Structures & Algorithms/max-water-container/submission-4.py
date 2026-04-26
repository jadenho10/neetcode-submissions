class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curArea = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                area = max(area, curArea)
                l += 1
            else:
                area = max(area, curArea)
                r -= 1
        return area
