class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Use a binary search method
        # Binary search all available rows in the matrix to find the right row 
            # Low = 0, High = len(matrix), Mid = Low + High // 2
            # ...basic binary search until range criteria is met
        # If the number is within the range of index 0 and index -1, then search the row
            # Implement a basic binary search for the row
            
        # Binary search for correct row
        low, high = 0, len(matrix) - 1
        targetRow = []
        
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                targetRow = matrix[mid]
                break
        
        # If targetRow is empty, then the value is out of bounds
        if not targetRow:
            return False
        
        # Binary search for correct value
        low, high = 0, len(targetRow) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if target < targetRow[mid]:
                high = mid - 1
            elif target > targetRow[mid]:
                low = mid + 1
            elif target == targetRow[mid]:
                return True
            
        return False
                
        