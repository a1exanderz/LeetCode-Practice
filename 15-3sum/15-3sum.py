class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Return all combinations of i, j, k triplets that sum to 0
        # Combinations cannot be duplicates
        
        output = []
        
        # First, sort the array, O(nlogn) time
        nums.sort()
        
        # Next, iterate through the sorted array, O(n^2) time
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            
            l, r = index + 1, len(nums) - 1
            
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return output
                        
        