# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
naive approach: 
set root as TreeNode(preorder[0])
find root idx in inorder arr # this takes O(N)
root.left = dfs(preorder[1: idx + 1], inorder[:idx])
root.right = dfs(preorder[idx + 1:], inorder[idx + 1])

O(N^2)

soln:
hashmap approach : store the {value : i for everything in inorder}
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder_vals = {num : i  for i, num in enumerate(inorder)}
        preIdx = 0
        # borders for subtrees to add nodes 
        # l, r are in [0, len(preorder)]
        def dfs(l, r):
            nonlocal preIdx
            if l > r:
                return None
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            rootIdx = inorder_vals[root.val] # location of root of tree in inorder arr 

            root.left = dfs(l, rootIdx - 1)
            root.right = dfs(rootIdx + 1, r)
            return root
        return dfs(0, len(preorder) - 1)
            

