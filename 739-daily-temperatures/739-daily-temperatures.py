class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force method is to loop through each value and loop again for the ith day. O(n^2) time.
        
        # Maintain a monotonic (decreasing) stack at all times
        # Initiate an output array of length of input array, initialized all to 0
        # Save the value and the index of each temperature in the stack
        # Add each temperature to the stack. If the stack will not be monotonic, pop and update the output, then add new temperature
        # Once the input array has been iterated through, return output array
        
        stack = [(temperatures[0], 0)]
        output = len(temperatures) * [0]
        
        for i in range(1, len(temperatures)):   
            while stack and stack[-1][0] < temperatures[i]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                
            stack.append((temperatures[i], i))
            
            # print(stack)
                            
        return output
        
        