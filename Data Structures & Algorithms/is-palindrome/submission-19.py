import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while (True):
            # check if i and j are letters/numbers.
            while (not ((ord(s[i])>=ord('0') and ord(s[i])<=ord('9')) or (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')) or (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')))):
                i+=1
                if (i>=len(s)):
                    return True
            while (not ((ord(s[j])>=ord('0') and ord(s[j])<=ord('9')) or (ord(s[j])>=ord('A') and ord(s[j])<=ord('Z')) or (ord(s[j])>=ord('a') and ord(s[j])<=ord('z')))):
                j-=1
                if (j<0):
                    return True

            print(f"{s[i].lower()} = {s[j].lower()}?")
            print(s[i].lower()==s[j].lower())
            if (s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
            if (i>j):
                break

        return True