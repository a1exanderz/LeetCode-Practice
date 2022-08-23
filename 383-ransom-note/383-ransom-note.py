class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Solution O(n)
        # Ransom string must be within magazine string
        # Construct a hashmap from the magazine O(m)
            # Hashmap should include key as letters and value as count
        # For each letter in ransomNote, subtract from the count in hashmap
            # If count ever goes below zero, return false
        
        hashMap = {}
        for c in magazine:
            if c in hashMap.keys():
                hashMap[c] += 1
            else:
                hashMap[c] = 1
                
        for c in ransomNote:
            if c not in hashMap.keys():
                return False
            else:
                hashMap[c] -= 1
                if hashMap[c] < 0:
                    return False
        
        return True