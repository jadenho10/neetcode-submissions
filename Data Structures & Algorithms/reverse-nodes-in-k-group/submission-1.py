# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gprev = dummy
            
        while True:
            kth = self.getKth(gprev, k)
            if not kth:
                break
            afterGroup = kth.next

            prev, curr = afterGroup, gprev.next
            while curr != afterGroup:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            tmp = gprev.next
            gprev.next = kth
            gprev = tmp
        return dummy.next
    
    #helper func to see how big our group is
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
