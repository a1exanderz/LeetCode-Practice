class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a sliding window method
        # Have a left and right pointer, l r
        # Iterate through the array with the right pointer
        # If the right pointer exists in the set, 
        
        
        # If there are no repeats, continue incrementing r. When there is a repeat, l = r and r += 1 (start again).
            # Repeats determined through a set
            # Save the max length
    
    
        maxLength = 0
        l = 0
        charSet = set()
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            # print(charSet)
            # print(r - l + 1)
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength
        
        # Optimized O(n^2) method