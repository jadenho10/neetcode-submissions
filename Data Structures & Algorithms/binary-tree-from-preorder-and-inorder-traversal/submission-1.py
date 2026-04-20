# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        hashmap = {num : i for i, num in enumerate(inorder)}
        preorderRoot = 0 
        def dfs(l, r):
            nonlocal preorderRoot
            if l > r:
                return None
            root = TreeNode(preorder[preorderRoot])
            preorderRoot += 1
            mid = hashmap[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder) - 1)