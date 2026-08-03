class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        shuffled = []

        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i+n])
        
        return shuffled