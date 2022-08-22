class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ### Solution: N is number of pixels, O(N) time, O(N) memory 
        # 1. Determine the starting pixel in the image using image[sr][sc]. If the starting pixel's color is fill color, return list.
        # 2. Store the color of the starting pixel (start_color). Then change its color to the fill color.
        # 3. Consider the 4-directional pixels. If they are the same color as start_color, change their color to fill color.
        # 4. Repeat for each subsequent valid pixel until no more additional pixels are valid.
        
        # Left right are -+ sc, same sr
        # Up down are -+ sr, same sc
        # Vertical length is len(image)
        # Horizontal length is len(image[sr])     
        
        start_color = image[sr][sc]
        
        if start_color == color:
            return image
        
        image[sr][sc] = color
        
        self.recursiveFlood(sr, sc, image, start_color, color)
        
        return image

        ###############
    def recursiveFlood(self, sr, sc, image, start_color, color):
        # print("sr:", sr, "sc:", sc)

        # Right flood
        if sc < len(image[sr])-1 and image[sr][sc+1] == start_color:
            # print("right flood")
            image[sr][sc+1] = color
            self.recursiveFlood(sr, sc + 1, image, start_color, color)

        # Left flood
        if sc > 0 and image[sr][sc-1] == start_color:
            # print("left flood")
            image[sr][sc-1] = color
            self.recursiveFlood(sr, sc - 1, image, start_color, color)

        # Up flood
        if sr > 0 and image[sr-1][sc] == start_color:
            # print("up flood")
            image[sr-1][sc] = color
            self.recursiveFlood(sr - 1, sc, image, start_color, color)

        # Down flood
        if sr < len(image)-1 and image[sr+1][sc] == start_color:
            # print("down flood")
            image[sr+1][sc] = color
            self.recursiveFlood(sr + 1, sc, image, start_color, color)
        
        
        
        