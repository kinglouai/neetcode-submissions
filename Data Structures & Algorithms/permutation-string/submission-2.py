class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=dict()
        d1=dict()
        for i in s1:
            d[i]=d.get(i,0)+1
            d1[i]=d1.get(i,0)+1
        l=0
        r=0
        while r<len(s2):
            if s2[r] in d:
                if d[s2[r]]>0:
                    d[s2[r]]-=1
                    r+=1
                else:
                    while d[s2[r]]<=0:
                        d[s2[l]]+=1
                        l+=1
            else:
                l=r+1
                r+=1
                d=d1.copy()
            if sum(d.values())==0:
                return True

        return False

        