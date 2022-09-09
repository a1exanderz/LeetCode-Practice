class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use a two pointer method from both ends, l and r
        # If sum is greater than target, decrement r
        # If sum is less than target, increment l
        # Do until l and r cross
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            diff = numbers[l] + numbers[r]
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            else:
                return [l + 1, r + 1]