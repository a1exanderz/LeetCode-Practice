class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # 1 1 1     # 2 1 2
        # 1 0 1     # 1 0 1
        # 1 1 1     # 2 1 2
        
        # 1 1 1     # 4 3 2     # 0,0 0,1 0,2
        # 1 1 1     # 3 2 1     # 1,0 1,1 1,2
        # 1 1 0     # 2 1 0     # 2,0 2,1 2,2
        
#         output = [[None]*len(mat) for i in range(len(mat))]
        
#         # First, go through the entire matrix and set all the 0s to 0s in the output
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 if mat[i][j] == 0:
#                     output[i][j] = 0
                    
#                     # Then, starting at that index in the output array, do a BFS while maintaining a level counter
#                     # If you come across a 1 (or in this case, None), set its value to the level counter
                    
#         return output
        
        
        ## Use a BFS queue
        # Process all 0-cells first, then 1-cells, using a queue to determine which order to process
        # Time = O(m*n) Space = O(m*n) for queue
        
#         m, n = len(mat), len(mat[0])
#         DIR = [0, 1, 0, -1, 0] # Used to BFS traverse, include "continue" to rule out certain cases
        
#         q = deque([])
        
#         for r in range(m):
#             for c in range(n):
#                 if mat[r][c] == 0:
#                     q.append((r, c))
#                 else:
#                     mat[r][c] = -1 # Which means it hasn't been processed
                    
#         while q:
#             r, c = q.popleft()
#             print("r", r, "c", c)
#             for i in range(4):
#                 nr, nc = r + DIR[i], c + DIR[i+1]
#                 if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
#                 print("True")
#                 mat[nr][nc] = mat[r][c] + 1 # Only if 1, updates its value to be the previous r and c's distance + 1
#                 q.append((nr, nc))
#         return mat

        ## Use a DP method
        # Use previous information to determine subsequent information
        # Since you need information from all 4 directions, do DP in two directions
        # Only compute for non-zeros
        # 1: Top left corner to bottom right corner, using top and left neighbors
        # 2: Bottom right corner, using bottom and right neighbors
        
        m, n = len(mat), len(mat[0])
        
        # First iteration
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    print("top", top, "left", left)
                    mat[r][c] = min(top, left) + 1
                    print(mat[r][c])
                    
        # Second iteration
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m - 1 else math.inf
                    right = mat[r][c+1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
                    
        return mat
                    
                
        
                    
                    
                    
            