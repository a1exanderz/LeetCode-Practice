class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for index, value in enumerate(nums):
        #     for index2 in range(index + 1, len(nums)):
        #         if target == value + nums[index2]:
        #             return (index, index2)
        
        ########################
        # using a hashmap: only need to run through the list once O(N) time
        # for each value in the list (eg 2) , see if target - value (eg 9-2, look for 7) appears in the list
        # looking through other values in the list using hashmap is O(1) time
        # so, the solution is O(N) time overall
        
        # For each value in the list, obtain the value of the (target - value) key that appears in the hashmap
        # Then, map the value of each number in the list to its index in the list
        
        hashmap = {}
        for index, value in enumerate(nums):
            if target-value in hashmap:
                return index, hashmap[target-value]
            hashmap[value] = index
            
        

        
        
            