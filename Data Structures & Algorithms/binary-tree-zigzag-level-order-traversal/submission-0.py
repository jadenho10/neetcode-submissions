# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = []
        if not root:
            return []
        q = deque([root])

        while q:
            size = len(q)
            array = [0] * size
            for i in range(size):
                node = q.popleft()
                idx = size - i - 1 if level % 2 else i
                array[idx] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            res.append(array)
        return res
