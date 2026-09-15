class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = {}

        for i in arr:
            if i not in occurence.keys():
                occurence[i] = 1
                continue
            occurence[i]+=1
        
        unique = {}

        for i in occurence.values():
            if i in unique.keys():
                return False
            unique[i] = 1
        return True