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


        def helper(root: Optional[TreeNode]): #rtype: NONE
            nonlocal res
            nonlocal count
            if root.left:
                helper(root.left)
            count -= 1
            if count == 0:
                res = root.val
            if root.right:
                helper(root.right)
        helper(root)
        return res
    