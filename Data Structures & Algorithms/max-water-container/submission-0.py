class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Start pointer at left and right 
        # Calculate area at each step
        # Move smaller height inward 
        # Terminate when 1 apart

        #--- TEST RUN ---# 

        # heights = [1,7,2,5,4,7,3,6] 
        # l = 5
        # r = 5
        # max_height = 36

        l = 0
        r = len(heights) - 1
        max_height = 0

        while r - l > 0: 

            max_height = max(max_height, self.calculate_area(l, r, heights)) 

            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1

        return max_height

    def calculate_area(self, l: int, r: int, heights: List[int]) -> int:

        w = r - l
        h = min(heights[l], heights[r])
        return w * h 
