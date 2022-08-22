# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # Basic Solution O(n) time, O(1) memory:
        # Call all values leading up to N starting from 1 and return value of the first "True"
        
        # if n == 1:
        #     return 1
        # else:
        #     i = 1
        #     while i <= n:
        #         if isBadVersion(i) == True:
        #             return i
        #         i += 1
        #     return -1
        
        # Optimized Solution: O(log(n)) time, O(1) memory
        # Use a binary search method
        l, r = 1, n
        
        while (l < r):
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l