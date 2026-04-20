# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = 0
        def inorder(root):
            nonlocal res
            nonlocal count
            if root.left:
                inorder(root.left)
            count -= 1
            if not count:
                res = root.val
            if root.right:
                inorder(root.right)
        inorder(root)
        return res
            