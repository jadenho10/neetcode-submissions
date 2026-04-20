# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) 
        curr = dummy 

        carry = 0 # represents surplus carry if val1 + val2 > 9
        while l1 or l2 or carry: # while both lists have stuff and carry != 0
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            newVal = value1 + value2 + carry
            # need to make sure newVal is not greater than 9

            carry = newVal // 10  #need to update carry 
            newVal = newVal % 10 # will return sum of first digits on the right
            curr.next = ListNode(newVal)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            curr = curr.next 
        return dummy.next


