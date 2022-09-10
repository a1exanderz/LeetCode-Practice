class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 6 4
        # Have two pointers (sliding window), l and r. 
        # If prices[l] > prices[r], slide both of them to the right
        # Otherwise keep incrementing r and save the profit and adjust maxProfit if needed
        # Continue until r is at end of array
        # O(n) time and O(1) space
        
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            while prices[l] > prices[r] and r < len(prices) - 1:
                l = r
                r += 1
            maxProfit = max(maxProfit, prices[r] - prices[l])
            # print("l", prices[l], "r", prices[r])
            r += 1
            
        return maxProfit
                