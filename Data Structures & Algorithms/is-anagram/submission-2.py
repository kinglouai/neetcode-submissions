class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=dict()
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]]=1
                elif s[i] in d:
                    d[s[i]]+=1
                if t[i] not in d:
                    d[t[i]]=-1
                elif t[i] in d:
                    d[t[i]]-= 1

            if list(d.values()).count(0)==len(d.values()):
                return True
            else:
                return False