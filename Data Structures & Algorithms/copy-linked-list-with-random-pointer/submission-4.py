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

'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        map = defaultdict(lambda : Node(0))
        map[None] = None
        curr = head
        while curr:
            map[curr].val = curr.val
            map[curr].next = map[curr.next]
            map[curr].random = map[curr.random]
            curr = curr.next
        return map[head]




