class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution: O(n) time and O(n) space
        # Find the majority threshold (n/2)
        # Add each new value to hashtable and count occurrences
        # At any point a value exceeds majority threshold you can return
        
#         majorityNum = math.ceil(len(nums) / 2)
#         hashtable = {}
        
#         if len(nums) == 1:
#             return nums[0]
        
#         for num in nums:
#             if num in hashtable.keys(): 
#                 hashtable[num] += 1
#                 if hashtable[num] >= majorityNum:
#                     return num
#             else:
#                 hashtable[num] = 1
                
        # Boyer Moore Algorithm O(n) time and O(1) space
        # Create two variables, curr (current value) and count (consecutive occurrences of curr)
        # Increment for every curr in the list and decrement for every non-curr in the list
        # If curr goes below 0, change curr to a new value
        
        curr, count = nums[0], 1
        # print("i", 0, "curr", curr, "count", count)
        for i in range(1, len(nums)):
            if curr == nums[i]:
                count += 1
            else:
                count -= 1
                if count < 0:
                    curr = nums[i]
                    count = 1
            # print("i", i, "curr", curr, "count", count)
        
        return curr
            
        
        
        
        
        