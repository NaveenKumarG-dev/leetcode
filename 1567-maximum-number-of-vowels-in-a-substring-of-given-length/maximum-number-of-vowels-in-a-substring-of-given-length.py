class Solution:

    def is_vowel(self,s):
        if s in "aeiou":
            return True
        else:
            return False

    def maxVowels(self, s: str, k: int) -> int:
        
        max = 0
        for i in s[:k]:
            if self.is_vowel(i):
                max+=1
        current = max

        for i in range(1,len(s)-k+1):
            if self.is_vowel(s[i-1]):
                current-=1
            if self.is_vowel(s[i+k-1]):
                current+=1

            max = current if current>max else max
        
        return max