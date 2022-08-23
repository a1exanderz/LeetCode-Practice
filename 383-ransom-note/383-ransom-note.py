class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Solution: O(n+m) time, O(m) memory, 15 minutes
        # Ransom string must be within magazine string
        # Construct a hashmap from the magazine O(m)
            # Hashmap should include key as letters and value as count
        # For each letter in ransomNote, subtract from the count in hashmap
            # If count ever goes below zero, return false
        
#         hashMap = {}
#         for c in magazine:
#             if c in hashMap.keys():
#                 hashMap[c] += 1
#             else:
#                 hashMap[c] = 1
                
#         for c in ransomNote:
#             if c not in hashMap.keys():
#                 return False
#             else:
#                 hashMap[c] -= 1
#                 if hashMap[c] < 0:
#                     return False
        
#         return True
    
        # Solution 2: O(n) time, O(m) memory
        # Iterate through the ransomNote and magazine in one loop
        # Construct a hashmap of the magazine, if ransomNote char is in it, subtract from count
        # Same conditions above, but in one loop
        # DOES NOT WORK: ransom letter could be present in later part of magazine string -- or you could use sorted
        
        if len(ransomNote) > len(magazine):
            return False
        
        ran = sorted(ransomNote)
        mag = sorted(magazine)
        
        for c in mag:
            if ran and c == ran[0]:
                ran.pop(0)
                
        if ran:
            return False
        else:
            return True
    