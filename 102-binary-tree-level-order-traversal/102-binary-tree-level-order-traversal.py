# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Use BFS on the tree, queue backed, and add values into lists
        # Queue: add to right, remove from left
        
        # For each element in the tree, add its children into the queue
        # When removing the values and adding to output array, add its children to queue
        # When queue is empty, problem is done
        
        output = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q) # Going through one level at a time
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                output.append(level)
            
        return output
            
            
    