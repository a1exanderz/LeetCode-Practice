class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution: O(n) time and O(n) space
        # Find the majority threshold (n/2)
        # Add each new value to hashtable and count occurrences
        # At any point a value exceeds majority threshold you can return
        
        majorityNum = math.ceil(len(nums) / 2)
        hashtable = {}
        
        if len(nums) == 1:
            return nums[0]
        
        for num in nums:
            if num in hashtable.keys(): 
                hashtable[num] += 1
                if hashtable[num] >= majorityNum:
                    return num
            else:
                hashtable[num] = 1