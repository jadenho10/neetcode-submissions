class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        water = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                water += maxR - height[r]
        return water