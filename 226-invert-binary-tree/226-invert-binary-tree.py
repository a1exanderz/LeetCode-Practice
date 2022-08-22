# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ### Solution: traverse each node down the tree using recursion and swap its children. O(N) runtime. O(N) memory used for the recursive stack.
        
        if not root:
            return None
        
        self.swapChildren(root)
        
        self.invertTree(root.left)
        self.invertTree(root.right)
            
        return root
        
    def swapChildren(self, node):
        temp = node.right
        node.right = node.left
        node.left = temp
        