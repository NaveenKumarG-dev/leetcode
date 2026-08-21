class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        seen = {}

        for i in nums:
            if i not in seen.keys():
                seen[i] = 0
            seen[i]+=1
        
        maximum = max(seen.values())
        frequency = 0
        for i in seen.values():
            if maximum == i:
                frequency += i
        
        return frequency
            