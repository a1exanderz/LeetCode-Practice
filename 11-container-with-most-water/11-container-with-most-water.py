class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Use a two pointer method, starting at both ends. Move away from the lower line.
        # Continually save the maxArea = max(maxArea, (r - l * min(height[l], height[r])))
        
        maxArea = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            # print(area)
        return maxArea

            
            