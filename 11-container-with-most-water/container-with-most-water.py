class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l=0
        r=len(height)-1
        while l<r:
            max_w = r-l
            min_h = height[r] if (height[l]>height[r]) else height[l]
            current_area = min_h*max_w

            max_area = max_area if max_area>current_area else current_area
            

            if height[l] == min_h:
                l+=1
            else:
                r-=1
        
        return max_area