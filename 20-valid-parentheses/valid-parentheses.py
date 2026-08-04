class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        
        for i in s:
            if i in pair.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    if pair[stack[-1]] == i :
                        stack.pop()
                    else:
                        return False 
        
        if stack == []:
            return True
        else:
            return False