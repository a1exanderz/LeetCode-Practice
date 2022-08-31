"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # Create a hashmap of all the connections
        # If a node is already in the hashmap, then no new copy is made and the old copy is returned as a neighbor
        # Copy the node and add all neighbors to the copy node using recursion
        
        hashTable = {}
        
        def dfs(node):
            if node in hashTable:
                return hashTable[node]
            
            copy = Node(node.val)
            hashTable[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node) if node else None
        