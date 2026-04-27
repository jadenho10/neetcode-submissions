"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
Output: Isomorphic one-to-one mapping from og to copy
Data structure that's great for 1-1 mappings: hashmap 
O(1) search 

A- A' - B - B' - C - C'

'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head

        # adding interleavings 
        # e.g. a - a' - b - b' 
        # a - a' - b
        # ^   ^
        while curr:
            copy = Node(curr.val, None, None)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        newHead = head.next # output later

        curr = head
        # fix all random ptrs in place
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # need to remove original list
        # a - a' - b - b' 
        # ^   ^
        curr = head
        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return newHead

            




