class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        occurence = {}
        result = []

        for i in nums:
            if i not in occurence.keys():
                occurence[i] = 1
                continue
            occurence[i]+=1
            result.append(i)
            
        return result