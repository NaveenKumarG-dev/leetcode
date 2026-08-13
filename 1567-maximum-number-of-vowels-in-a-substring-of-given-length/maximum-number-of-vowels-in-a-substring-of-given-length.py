class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        
        current = 0

        for i in range(k):
            if s[i] in vowels:
                current += 1

        maximum = current

        for i in range(1, len(s)-k+1):
            if s[i - 1] in vowels:
                current -= 1

            if s[i+k-1] in vowels:
                current += 1

            maximum = max(maximum, current)

        return maximum