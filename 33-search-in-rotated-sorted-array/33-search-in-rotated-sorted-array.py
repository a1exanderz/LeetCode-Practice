class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Target = 6
        
        # l,m,r = 0,3,6
        # 6 7 0 1* 2 4 5 
        # l,m,r = 4,5,6 ### checkRight = true
        # 6 7 0 1 2 4* 5
        # l,m,r = 6,6,6 ### since value not found, check left
        # 6 7 0 1 2 4 5*
        # l,m,r = 0,1,2
        # 6 7* 0 1 2 4 5
        # l,m,r = 0,0,0
        # 6* 7 0 1 2 4 5 ### value found, return
                         ### checkLeft = true
        
        
        l, r = 0, len(nums) - 1
        # print("start", l, (l + r) // 2, r)
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # Check direction of first search. If target <= rightmost if right, or target >= leftmost if left, then proceed. Otherwise try opposite side.
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
        return -1
                
        # Target 3
        # [4,5,6,7,8,1,2,3]
        # Check right
        # [4,5,6,7,8,1*,2,3]
        # 
        
        
        
        
        
