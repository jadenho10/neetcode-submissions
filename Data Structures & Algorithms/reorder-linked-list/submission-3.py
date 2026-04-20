# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
