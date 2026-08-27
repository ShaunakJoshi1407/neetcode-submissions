# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque([root])

        while q:
            levels = []
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if len(res) % 2:
                levels.reverse()
            res.append(levels)
        return res