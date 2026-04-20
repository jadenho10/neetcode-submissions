# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
digits are stored in opposite order
want to add nodes and produce sum

edge case: 9 + 9 = 8 -> 1

'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0 #either 1 or 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0 
            newVal = l1_val + l2_val + carry

            carry = newVal // 10
            newVal %= 10

            curr.next = ListNode(newVal) 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next
