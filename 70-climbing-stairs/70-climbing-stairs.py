class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution:
        # Break into subproblems
        # Base: 1
        # To reach Step 1: 1 step
        # To reach Step 2: 1+1 step or 2 steps
        # To reach Step 3: 1+1+1 steps or 1+2 steps or 2+1 steps
        # To reach Step 4: 1+1+1+1 steps or 1+2+1 steps or 1+1+2 steps or 2+1+1 steps or 2+2 steps
        # To reach Step 5: 1+1+1+1+1 steps or 1+2+1+1 steps or 1+1+2+1 steps or 2+1+1+1 steps or 1+1+1+2 steps or 2+2+1 steps or 2+1+2 steps or 1+2+2 steps
        # i.e. Fib sequence?
        
        memo, i = [1, 1], 2
        while i <= n:
            print(i, memo)
            memo.append(memo[i-2] + memo[i-1])
            i += 1
        
        return memo[-1]