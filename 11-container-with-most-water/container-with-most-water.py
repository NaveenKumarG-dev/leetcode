class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            width = r - l
            min_height = min(height[l], height[r])
            current_area = width * min_height

            max_area = max(max_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area