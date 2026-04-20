class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in hashmap: 
                return [hashmap[diff], n]
            hashmap[nums[n]] = n
            
        
         

        