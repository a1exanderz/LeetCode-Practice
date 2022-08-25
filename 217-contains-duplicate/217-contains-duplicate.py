class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Solution: 0(n) time and O(n) space
        # For the entire list, add a value to the dictionary if it doesn't exist
        # If the value already exists, return True
        # If the entire loop runs, return False
        # We use a dictionary for O(1) retrieval, vs. list which would take longer
        
        hashTable = {}
        
        for num in nums:
            if num in hashTable.keys():
                return True
            else:
                hashTable[num] = 1
                
        return False