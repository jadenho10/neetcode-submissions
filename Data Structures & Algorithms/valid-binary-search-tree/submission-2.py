# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Do recursive dfs. Every node must fit a valid range

children on left must be less than parent,
children on right must be greater than parent
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(left, root, right):
            # base cases
            if not root:
                return True
            if not (left < root.val < right):
                return False
            # recursive dfs left and right children
            return isValid(left, root.left, root.val) and isValid(root.val, root.right, right)
        return isValid(float('-inf'), root, float('inf'))

            