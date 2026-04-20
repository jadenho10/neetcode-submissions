# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
New Value DNE in og BST

properties of BST: left subtree vals < root.val < right subtree vals

recursively enter the tree

dfs()
if not root:
    return TreeNode(val)

if val > root.right
    root.right = dfs(root.right)
else val < root.right
    root.left = dfs(root.right)

example 1:
6
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

        