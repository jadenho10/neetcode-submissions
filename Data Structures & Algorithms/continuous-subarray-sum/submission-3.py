'''
hashmap for prefix sums

hashmap for: remainder : index
 
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0 : -1  } # remainder : idx
        remainder = 0

        for i, num in enumerate(nums):
            remainder = (num + remainder) % k
            
            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i
        return False