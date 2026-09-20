class Solution:
    def twoSum(self, nums: list[int], target: int) -> lidxdxst[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]
            seen[num] = idx