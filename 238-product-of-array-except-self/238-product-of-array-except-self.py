class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ## Make an output array that is the prefix array first
        output = [1]
        
        for i in range(len(nums) - 1):
            output.append(nums[i] * output[i])
        
        # print(output)
        
        # 1 2 3 4
        # 1 1 2 6
        # 24 12 8 6
        
        # -1 1 0 -3 3
        # 1 -1 -1 0 0
        # 0 0 9 0 0
        
        ## Iterate through the output array in reverse order while saving a continually updated suffix value 
        suffix = 1
        
        for i in range(len(output) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output