class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        string = [c for c in s if c.isalnum()]
        return string == string[::-1]