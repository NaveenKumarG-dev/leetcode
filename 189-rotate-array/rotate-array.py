from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        d = deque(nums)
        d.rotate(k)
        nums[:] = d