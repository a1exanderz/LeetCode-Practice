class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Use a hash table. If the value already exists in hash table, return True
        # Otherwise return False if iterated through the entire array
        
        hashTable = {}
        
        for num in nums:
            if num in hashTable.keys():
                return True
            else:
                hashTable[num] = 1
                
        return False