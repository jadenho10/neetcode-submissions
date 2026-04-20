# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0 1 2 3 4 5 6

0 6 1 5 2 4 3
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # we want to retrieve middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of list
        curr, prev = slow, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None

        left, right = head, prev #left, right halves of linked list
        while right.next:
            leftNext = left.next
            left.next = right
            left = leftNext

            rightNext = right.next
            right.next = left
            right = rightNext