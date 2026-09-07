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
        
        q = collections.deque([root])

        res = []

        while q:
            levels = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if len(res) % 2:
                levels = levels[::-1]
            
            res.append(levels)

        return res