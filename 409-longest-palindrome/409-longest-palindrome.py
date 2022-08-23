class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Solution: O(2n) time, O(n) memory
        # If length 1, return 1
        # Only one odd count can exist, and rest have to be even
        # For all even counts in string, add their entire value
        # If there are multiple odd counts, the highest odd count add their entire value
            # All other odd counts add their entire value - 1
        
        if len(s) == 1:
            return 1
        
        hashTable = {}
        for char in s:
            if char in hashTable.keys():
                hashTable[char] += 1
            else:
                hashTable[char] = 1
        
        totalLength = 0
        odd = False
        for key in hashTable:
            if hashTable[key] % 2 == 0:
                totalLength += hashTable[key]
            if hashTable[key] % 2 == 1:
                odd = True
                totalLength += hashTable[key] - 1
            
        if odd:
            totalLength += 1
            
        return totalLength
        
        
        