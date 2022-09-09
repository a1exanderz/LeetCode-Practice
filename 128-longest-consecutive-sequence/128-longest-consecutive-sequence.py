class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a set (hashTable), O(n) time
        # Each subsequence starts with a value without a left consecutive value
        
        numsSet = set(nums)
        
        subSeq = {}
        longest = 0
        for num in nums:
            if (num - 1) not in numsSet:
                subSeq[num] = 1
                incNum = num + 1
                while incNum in numsSet:
                    subSeq[num] += 1
                    incNum += 1
                longest = max(longest, subSeq[num])
                
        return longest
        