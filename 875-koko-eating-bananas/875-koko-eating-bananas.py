class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = 8
        # 3 6 7 11, sorted
        # k = (3+11)/2 = 7 
        # 1, 1, 1, 2 < 8
        # k = (3+6)/2 = 4
        # IF YOU TRY 6
        # 1, 1, 2, 2 = 6
        # IF YOU TRY 3
        # 1, 2, 3, 4 = 10
        
        # h = 6
        # 4 11 20 23 30
        # k = (1+30)/2 = 15
        # 1, 1, 2, 2, 2 > 6
        # k = (16+30)/2 = 23
        # 1, 1, 1, 1, 2 == 6
        
        # Brute force: test every integer starting from 1. The closest k >= h is the output
        
        # Optimized way: use some form of binary search, testing all discrete integers (piles[i]/k, round up)
        # First sort the array, then test all values of k using binary search. Closest k >= h is the output
        
        # Use number values, rather than the index
        # If you reach an answer that is == h, keep trying smaller numbers until the next one is not it, then return the minimum
        
        
        # Binary search
        low, high = 1, max(piles)
        output = high
        while low <= high:
            time = 0
            mid = (low + high) // 2
            # print("mid", mid)
            for pile in piles:
                time += math.ceil(pile / mid)
            #     print(math.ceil(pile / mid))
            # print("time", time)
            if time > h:
                low = mid + 1
            elif time <= h:
                output = min(output, mid)
                high = mid - 1
        
        return output
        
        
        
        
        