'''
find duplicate number:
each num is in [1, n] with n being length of array

each int appears once except for one int

need to solve without modifying nums and O(1)
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        curr = 0
        while True:
            slow = nums[slow]
            curr = nums[curr]
            if slow == curr:
                return curr