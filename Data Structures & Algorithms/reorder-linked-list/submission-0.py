# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:\
        # get the middle pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse linked list
        curr, prev = slow.next, None 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None
        
        #merge two linked lists
        head1, head2 = head, prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next

        
        



        

        

        
        
        