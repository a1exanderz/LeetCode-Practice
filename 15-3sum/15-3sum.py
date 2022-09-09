class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution explanation: 
        # Sort the array to prevent starting with the same value (imagine a + b + c for threeSum, no repeat a's)
        # Increment through the sorted array without repeating values (if num == prev num, continue)
        # Then, use left and right pointers for the remainder of the array to determine values for b and c
        # If a + b + c = 0, then save to array, otherwise increment or decrement based on distance from 0
        
        sortedNums = sorted(nums)
        output = []
        
        for index, a in enumerate(sortedNums):
            # Prevents starting with the same value
            if index > 0 and a == sortedNums[index - 1]:
                continue
            
            b, c = index + 1, len(nums) - 1
            while b < c:
                threeSum = a + sortedNums[b] + sortedNums[c]
                if threeSum > 0:
                    c -= 1
                elif threeSum < 0:
                    b += 1
                else:
                    output.append([a, sortedNums[b], sortedNums[c]])
                    b += 1
                    while sortedNums[b] == sortedNums[b - 1] and b < c:
                        b += 1
                        
        return output
                    
                    