class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracks = ["(", "{", "["]
        closeBracks = [")", "}", "]"]

        if len(s)==1: return False

        for i in range(len(s)):
            if (s[i] in openBracks):
                stack.append(s[i])
            elif (s[i] in closeBracks):
                if len(stack)==0:
                    return False
                if (openBracks.index(stack.pop()) != closeBracks.index(s[i])):
                    return False
        
        if len(stack)!=0:
            return False
        return True