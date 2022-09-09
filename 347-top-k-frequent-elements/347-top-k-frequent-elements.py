class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a hashMap of the nums array in O(n) time
        
        hashMap = {}
        
        for num in nums:
            if num not in hashMap.keys():
                hashMap[num] = 1
            else:
                hashMap[num] += 1
                
        sortItems = sorted(hashMap.items(), key = lambda x:x[1], reverse = True)
  
        # print(sortItems)

        output = []
        for i in range(k):
            output.append(sortItems[i][0])
        
        return output
            
        
        
        