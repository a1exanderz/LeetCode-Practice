# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         ### Solution 1:
#         # Store each pathway to each node. O(log(n)) time and space
#         # Compare both pathways: the node before first instance where the nodes are not equal is our answer O(log(n)) time and O(1) space
        
#         # Retrive pathway for P
#         initRoot = root
#         pathP = [initRoot]
        
#         while initRoot.val != p.val:
#             if initRoot.val > p.val:
#                 initRoot = initRoot.left
#                 pathP.append(initRoot)
#             else:
#                 initRoot = initRoot.right
#                 pathP.append(initRoot)
                
#         # Retrive pathway for Q
#         initRoot = root
#         pathQ = [initRoot]
        
#         while initRoot.val != q.val:
#             if initRoot.val > q.val:
#                 initRoot = initRoot.left
#                 pathQ.append(initRoot)
#             else:
#                 initRoot = initRoot.right
#                 pathQ.append(initRoot)
                
#         # Compare both lists and return either the first equal node value where the next node is not equal
#         # Or the last value of the smallest list
#         smallestListLen = min(len(pathP), len(pathQ))
        
#         for i in range(0, smallestListLen):
#             try:
#                 if pathP[i+1] != pathQ[i+1]:
#                     return pathP[i]
#             except:
#                 return pathP[i]
        
        ### Solution 2: 
        # More efficient code
        
        initRoot = root
        
        while initRoot:
            if p.val > initRoot.val and q.val > initRoot.val:
                initRoot = initRoot.right
            elif p.val < initRoot.val and q.val < initRoot.val:
                initRoot = initRoot.left
            else:
                return initRoot
            
                
            