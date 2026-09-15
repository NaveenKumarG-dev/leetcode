class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        occurence = {}

        for i in range(len(nums)):
            if nums[i] not in occurence.keys():
                occurence[nums[i]] = [i]
                continue
            
            occurence[nums[i]].append(i)

            if abs(occurence[nums[i]][-2] - occurence[nums[i]][-1]) <= k:
                return True
        
        return False