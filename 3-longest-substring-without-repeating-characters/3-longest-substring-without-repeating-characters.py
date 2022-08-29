class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Simple solution: O(n^2) time, O(1) space
        # For each letter in the string, check each subsequent letter until there is a repeat
        # Return the max
        
        maxLength = 0
        for i, c in enumerate(s):
            length = 1
            # print("index", i, "character", c)
            i += 1
            hashTable = {}
            hashTable[c] = None
            if i + maxLength < len(s) + 1:
                while i < len(s) and s[i] not in hashTable.keys():
                    hashTable[s[i]] = None
                    # print("hashtable", hashTable, "new index", i, "next character", s[i])
                    length += 1
                    # print("length", length)
                    i += 1
            maxLength = max(length, maxLength)
        
        return maxLength
    
        # Need a faster solution
                