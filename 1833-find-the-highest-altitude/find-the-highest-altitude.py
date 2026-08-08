class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        sum = 0
        for num in gain:
            sum+=num
            altitude.append(sum)
        return(max(altitude))