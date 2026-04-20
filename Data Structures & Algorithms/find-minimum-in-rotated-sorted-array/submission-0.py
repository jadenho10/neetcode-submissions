class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float('inf')
        for i in range(len(nums)):
            curNum = nums[i]
            minNum = min(minNum, curNum)
        
        return minNum
            
        