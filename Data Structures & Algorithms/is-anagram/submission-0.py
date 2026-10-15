class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dihh = dict()

        for i in range(len(s)):
            x = s[i]
            if x in dihh.keys():
                dihh[x]=dihh[x]+1
            else:
                dihh[x] = 1
        
        print(dihh)
        
        for i in range(len(s)):
            x=t[i]
            if x not in dihh.keys() or dihh[x]<=0:
                return False
            else:
                dihh[x] = dihh[x]-1
        
        return True
