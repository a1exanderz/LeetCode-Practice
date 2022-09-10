class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 6 4
        # Have two pointers (sliding window), l and r. 
        # If prices[l] > prices[r], slide both of them to the right
        # Otherwise keep incrementing r and save the profit and adjust maxProfit if needed
        # Continue until r is at end of array
        # O(n) time and O(1) space
        
        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit
                