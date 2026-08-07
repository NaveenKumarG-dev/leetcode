class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = []
        sum = 0
        
        for num in nums:
            sum = sum + num
            running_sums.append(sum)

        return running_sums