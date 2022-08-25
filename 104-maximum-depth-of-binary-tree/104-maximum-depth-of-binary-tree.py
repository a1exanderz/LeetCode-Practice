# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Maximum depth = height
        # Use a recursive height solver
        
        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        return height(root)