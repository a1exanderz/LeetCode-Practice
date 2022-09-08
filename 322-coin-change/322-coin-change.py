class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # First sort the coins array, O(n*log(n)) time using python's default sort
        coinsSorted = sorted(coins)
        
        # If the largest coin can be subtracted from the amount, then do so and increment output
        # If not, iterate through coinsSorted until the value can be subtracted from the amount, and increment
        # Do so until the amount is 0
        # Greedy solution
        
#         output = 0
#         amountLeft = amount
        
#         for i in range(len(coinsSorted) - 1, -1, -1):
#             while (amountLeft - coinsSorted[i]) >= 0:
#                 output += 1
#                 amountLeft -= coinsSorted[i]
#             print("i", i, "aL", amountLeft, "output", output)
        
#         if amountLeft != 0:
#             return -1
#         else:    
#             return output
        
        # 6249 - 419*14 = 383       c 14
        # 383 - 186*2 = 11          c 16
        # OR 
        # 383 - 83*4
        
        # The issue is that you're exhausting the largest coin value, which may not always lead to 0. 
        # Sometimes using only some of the largest coin value is necessary.
        # Greedy solution doesn't work
        # DP method?
        
        
        ############# DP METHOD ##############
        # Compute the minimum coins needed for each integer up to the amount variable
        # Use previous values to determine new value
        # Return the final index of the DP array, which contains the min coins for the length
        
        # Start with a DP array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # print(dp)
        
        # Compute every value in DP
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    
                    ## This is most important step
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                    
                    # print(dp)
                    
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
                    
        # Time = O(amount * len(coins))
        # Space = O(amount)
        