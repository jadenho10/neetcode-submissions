# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we know its a binary search tree

inorder traversal -> gives us ascending order of array 

can pick off kth val with inorder traversal

'''


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        count = k
        def inorder(root):
            nonlocal res
            nonlocal count
            if root.left:
                inorder(root.left)

            count -= 1
            if count == 0:
                res = root.val
            
            if root.right:
                inorder(root.right)
        inorder(root)
        return res
            

