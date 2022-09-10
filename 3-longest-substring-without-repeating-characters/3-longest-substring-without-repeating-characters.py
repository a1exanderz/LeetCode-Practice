class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a sliding window method
        # Have a left and right pointer, l r
        # If there are no repeats, continue incrementing r. When there is a repeat, l = r and r += 1 (start again).
            # Repeats determined through a set
            # Save the max length
        
        if len(s) == 0:
            return 0
        
        maxLength = 1
        l, r = 0, 1
        
        while r < len(s):
            unique = set({s[l]})
            length = 1
            while r < len(s) and s[r] not in unique:
                length += 1
                maxLength = max(maxLength, length)
                unique.add(s[r])
                r += 1
            # print("l", l, "r", r, unique)
            l += 1
            r = l + 1
            
        return maxLength
    
    # dvdf
    # dv 
            
        