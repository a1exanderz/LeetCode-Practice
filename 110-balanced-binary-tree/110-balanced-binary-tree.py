# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Basic solution: do DFS on each node to determine whether it is balanced
        # DFS to obtain height
        # DFS is O(n), and with n nodes, that is a O(n^2) solution
       
        def findHeight(root):
            if root is None:
                return 0
            return 1 + max(findHeight(root.left), findHeight(root.right))
        
        def eachNodeBalanced(root):
            if root is None:
                return True
            print(root.val)
            if abs(findHeight(root.left) - findHeight(root.right)) <= 1 and eachNodeBalanced(root.left) and eachNodeBalanced(root.right):
                return True
            return False
        
        return eachNodeBalanced(root)
        
        # Optimized approach: O(n) time
        # Learn how to do the bottom up method
            # If both leaf nodes are balanced, obtain their heights while you are at it.
            # Then, use their heights to determine if their parent node is balanced
            
        
        
        
        
        
        
        