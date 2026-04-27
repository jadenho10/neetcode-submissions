# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0, 1, 2, 3, 6, 5, 4
h           p     
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        l1, l2 = head, prev  
        while l2.next:
            next1 = l1.next
            l1.next = l2
            l1 = next1

            next2 = l2.next
            l2.next = l1
            l2 = next2
        
