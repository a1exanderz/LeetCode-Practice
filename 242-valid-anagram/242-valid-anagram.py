class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         ### Solution: create a hash table that contains the number of occurrences of each letter in the first string.
#         # Then, create a second hash table for the second string
#         # Compare the key value pairs for both hashmaps. If one doesn't match, terminate and return false. If all match, return true.
        
        # Optimization: if length not the same, immediately return false
        if len(s) != len(t):
            return False
        
        hash_map1 = {}
        # Create a hashmap for first string, O(N)
        for char in s:
            if char not in hash_map1:
                hash_map1[char] = 1
            elif char in hash_map1:
                hash_map1[char] += 1
        
        hash_map2 = {}
        # Create a hashmap for the second string, O(M)
        for char in t:
            if char not in hash_map2:
                hash_map2[char] = 1
            elif char in hash_map2:
                hash_map2[char] += 1

        # Then test for equivalence between both hashmaps: O(N) if N=M, and O(1) if their number of items is different
        return hash_map1 == hash_map2
        
#         # Runtime: O(N). Memory: O(N)
        
#         ### Solution 2: Improve memory to O(1) but possibly at the cost of runtime
#         # Sort each string and compare their equality. Sorting will take O(1) memory and O(N^2) time or O(NlogN) if optimized. Comparing will take O(N) time. 
        
#         return sorted(s) == sorted(t)
    
#         ### Solution 3: Use pythons counter function
        
#         return Counter(s) == Counter(t)
            
            
                
        