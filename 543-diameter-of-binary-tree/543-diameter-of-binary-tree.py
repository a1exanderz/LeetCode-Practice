# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Diameter: the furthest node on the left and the furthest node on the right, for each node
        
        # Obtaining the diameter for a node: 
        # Finding the maximum height on the left and maximum height on the right
        
        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        def diameter(root):
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            diameter = leftHeight + rightHeight
            return diameter
        
        maxDiameter = []
        
        # Traverse through each node in the binary tree
        
        def dfs(root, maxDiameter):
            if root is not None:
                if diameter(root) not in maxDiameter:
                    maxDiameter.append(diameter(root))
                dfs(root.left, maxDiameter)
                dfs(root.right, maxDiameter)
            return max(maxDiameter)
                
        return dfs(root, maxDiameter)
        


    

    
        

        
        
            