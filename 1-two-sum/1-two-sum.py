class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a hashmap, key = num and value = index
        # Iterate through each value of the array. If the difference between the value and target is not in the hashmap, add value to hashmap.
        # Eventually, the difference will be found in the hashmap
        
        hashMap = {}
        for index, num in enumerate(nums):
            if (target - num) not in hashMap.keys():
                hashMap[num] = index
            else:
                return [index, hashMap[target - num]]
                