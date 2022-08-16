class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         ### Solution 1: O((n^2)/2) time O(n^2) memory
#         # Create a 2D array as shown below
#         # Keep the max value and return when done
#         ## Time limit exceeded
        
#         # [-2] -> [-1] -> [-4] -> [ 0] -> [-1] -> [ 1] -> [ 2] -> [-3] -> [ 1]
#         #         [ 1] -> [-2] -> [ 2] -> [ 1] -> [ 3] -> [ 4] -> [-1] -> [ 3]
#         #                 [-3] -> [ 1] -> [ 0] -> [ 2] -> [ 3] -> [-2] -> [ 2]
#         #                         [ 4] -> [ 3] -> [ 5] -> [*6] -> [ 1] -> [ 5]
#         #                                 [-1] -> [ 1] -> [ 2] -> [-3] -> [ 1]
#         #                                         [ 2] -> [ 3] -> [-2] -> [ 2]
#         #                                                 [ 1] -> [-4] -> [ 0]
#         #                                                         [-5] -> [-1]
#         #                                                                 [ 4]
        
#         max_sum = nums[0]
#         array = [[0]*len(nums) for i in range(len(nums))] 
#         array[0][0] = nums[0]
        
#         for num in range(1, len(nums)):
#             for i in range(0, num+1):
#                 array[i][num] = nums[num] + array[i][num-1]
#                 if array[i][num] > max_sum:
#                     max_sum = array[i][num]
                    
#         return max_sum

        ### Solution 2: O(n)
        # Use a double pointer method. Left index moves only if the subarray sum is negative, and right index constantly moves.
        # With both indexes, compute the sum of the subarray, if max, set as max
        
        max_sum = nums[0]
        sub_sum = 0
        
        for n in nums:
            if sub_sum < 0:
                sub_sum = 0
            sub_sum += n
            # print("n", n, "sub_sum", sub_sum)
            max_sum = max(max_sum, sub_sum)
             
        return max_sum