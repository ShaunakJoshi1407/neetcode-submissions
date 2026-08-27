# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])

        res = []

        while q:
            levels = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if levels:
                res.append(levels)
        return res