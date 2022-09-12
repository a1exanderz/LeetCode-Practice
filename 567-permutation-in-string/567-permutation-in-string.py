class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Can exclude all cases where s1 length > s2 length
        if len(s1) > len(s2):
            return False
        
        # Sliding window method, len of window is len of s1
        # For each window, check to see if the permutation matches 
            # You can either sort both strings and check equality
            # Or compare hash tables O(2n)
            
        # Create s1 hash to compare to s2. O(len(s1)) time and space
        s1_hash = {}
        for c in s1:
            if c not in s1_hash.keys():
                s1_hash[c] = 1
            else:
                s1_hash[c] += 1
        
        # Initialize s2 hash table and test first case
        l, r = 0, len(s1) - 1
        s2_hash = {}
        
        for c in s2[l:r+1]:
            if c not in s2_hash.keys():
                s2_hash[c] = 1
            else:
                s2_hash[c] += 1
                
        if s1_hash == s2_hash:
            return True
        else:
            s2_hash[s2[l]] -= 1
            if s2_hash[s2[l]] <= 0:
                del s2_hash[s2[l]]
            l += 1

        # Iterate through s2 string with sliding window method. O(len(s2)) time
        # s2_hash stores the substring in a hash. O(len(s1)) space
        for r in range(len(s1), len(s2)):
            
            # print(s2[l:r+1])
            
            if s2[r] not in s2_hash.keys():
                s2_hash[s2[r]] = 1
            else:
                s2_hash[s2[r]] += 1
            
            # print(s2_hash)
            
            # Comparing two hash tables is O(len(s1)) time
            if s1_hash == s2_hash:
                return True
            else:
                s2_hash[s2[l]] -= 1
                if s2_hash[s2[l]] <= 0:
                    del s2_hash[s2[l]]
                l += 1
            
        return False
            