class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l = 0
        r = len(nums)-1
        squared = []

        while l<=r:
            if nums[l]**2>nums[r]**2:
                squared.append(nums[l]**2)
                l+=1
            else:
                squared.append(nums[r]**2)
                r-=1
        
        return squared[::-1]
            
