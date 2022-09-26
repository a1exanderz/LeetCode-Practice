class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
#         ### Iterative Solution
#         l, h = 0, len(nums) - 1
        
#         while l <= h:
#             m = (l + h) // 2
#             if nums[m] == target:
#                 return m
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 h = m - 1
        
#         return -1

        ### Recursive Solution
        low, high = 0, len(nums) - 1
        
        def binarySearch(low, high):
            if high >= low:
                mid = (low + high) // 2
                if target > nums[mid]:
                    return binarySearch(mid + 1, high)
                elif target < nums[mid]:
                    return binarySearch(low, mid - 1)
                else:
                    return mid
            else:
                return -1
        
        return binarySearch(low, high)
        