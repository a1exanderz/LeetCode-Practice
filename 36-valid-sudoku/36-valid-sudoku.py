class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain 1-9 without repetition
            # Use a set
        # Each column must contain 1-9 without repetition
            # Use row algorithm on transposed matrix
        # Each sub-boxes must not contain repetition
            # Create 3 different sets that are reset after 3 row iterations
            
        # Row
        rowUnique = self.determineRowUnique(board)
        
        # Column
        transposedBoard = zip(*board)
        columnUnique = self.determineRowUnique(transposedBoard)
        
        # Sub-boxes
        
        return rowUnique and columnUnique
        
    def determineRowUnique(self, matrix):
        
        subBoxUnique1, subBoxUnique2, subBoxUnique3 = set({}), set({}), set({})
        subBoxCounter = 0
        
        for row in matrix:
            rowUnique = set({})
            
            if subBoxCounter == 3:
                subBoxCounter = 0
                subBoxUnique1, subBoxUnique2, subBoxUnique3 = set({}), set({}), set({})
            
            for index, num in enumerate(row):                
                if num != ".":
                    if 0 <= index <= 2:
                        if num in subBoxUnique1:
                            return False
                        subBoxUnique1.add(num)
                    elif 3 <= index <= 5:
                        if num in subBoxUnique2:
                            return False
                        subBoxUnique2.add(num)
                    else:
                        if num in subBoxUnique3:
                            return False
                        subBoxUnique3.add(num)
                    
                    
                    if num in rowUnique:
                        return False
                    else:
                        rowUnique.add(num)
                        
            subBoxCounter += 1
                
            # print("1", subBoxUnique1)
            # print("2", subBoxUnique2)
            # print("3", subBoxUnique3)
                
        return True
    
    
    