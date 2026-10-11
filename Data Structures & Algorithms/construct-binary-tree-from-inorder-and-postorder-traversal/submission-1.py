# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def dfs(l, r):
            if l > r:
                return
            
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1
            mid = indices[root_val]
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)
            return root

        return dfs(0, len(postorder) - 1)