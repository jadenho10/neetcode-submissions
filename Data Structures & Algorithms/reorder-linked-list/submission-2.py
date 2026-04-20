# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur, prev = slow.next, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        slow.next = None

        #merge linked lists
        head1, head2 = head, prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next
        
        
        



        

        

        
        
        