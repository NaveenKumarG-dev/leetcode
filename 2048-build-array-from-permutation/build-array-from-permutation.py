class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        permutation = []

        for i in range(len(nums)):
            permutation.append(nums[nums[i]])

        return(permutation)