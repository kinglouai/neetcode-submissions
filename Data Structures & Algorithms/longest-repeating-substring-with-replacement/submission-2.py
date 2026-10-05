class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=dict()    
        x=0
        y=0
        m=0
        while y<len(s):
            d[s[y]]=d.get(s[y],0)+1
            c=(y-x+1)-max(d.values())
            if c<=k:
                m=max(m,(y-x+1))
                y+=1
            else:
                while (y-x+1)-max(d.values())>k:
                    d[s[x]]-=1
                    x+=1
                y+=1

            
        return m


