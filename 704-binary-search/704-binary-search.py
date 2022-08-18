class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Implement a traditional binary search algorithm on a sorted list (can do iteratively or recursively).
        # Start from the middle index. If the target is higher than the middle index, search using the sublist above, and vice versa if target is below.
        # Continue until target is found (m_index == target), or if not, return -1.
        
        ### Recursive Method: Time = O(log(n))
        
        low = 0
        high = len(nums) - 1
        
        def binary(low, high):
            if high >= low:
                mid = (low + high) // 2
        
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    return binary(mid + 1, high)
                else:
                    return binary(low, mid - 1)

            else:
                return -1
            
        return binary(low, high)