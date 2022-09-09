class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a set (hashTable), O(n) time
        # Each subsequence starts with a value without a left consecutive value
        
        numsSet = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in numsSet:
                incNum = num + 1
                while incNum in numsSet:
                    incNum += 1
                longest = max(longest, incNum - num)
                
        return longest
        