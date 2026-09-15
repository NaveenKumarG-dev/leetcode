class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        occurence = {}

        for i in nums:
            if i not in occurence.keys():
                occurence[i] = 1
                continue
            occurence[i]+=1
        sum = 0

        for i in occurence.keys():
            if occurence[i] == 1:
                sum+=i

        return sum