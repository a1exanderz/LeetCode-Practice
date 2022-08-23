class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution O(n) time, O(n) memory:
        # Break into subproblems
        # Base: 1
        # To reach Step 1: 1 step
        # To reach Step 2: 1+1 step or 2 steps
        # To reach Step 3: 1+1+1 steps or 1+2 steps or 2+1 steps
        # To reach Step 4: 1+1+1+1 steps or 1+2+1 steps or 1+1+2 steps or 2+1+1 steps or 2+2 steps
        # To reach Step 5: 1+1+1+1+1 steps or 1+2+1+1 steps or 1+1+2+1 steps or 2+1+1+1 steps or 1+1+1+2 steps or 2+2+1 steps or 2+1+2 steps or 1+2+2 steps
        # i.e. Fib sequence?
        
#         memo, i = [1, 1], 2
#         while i <= n:
#             memo.append(memo[i-2] + memo[i-1])
#             i += 1
        
#         return memo[-1]
    
    
        # Solution with O(1) memory:
        
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one