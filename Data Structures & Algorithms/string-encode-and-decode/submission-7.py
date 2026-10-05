class Solution:

    def encode(self, strs: List[str]) -> str:
        s1=""
        s2=""
        for i in strs:
            s1+=str(len(i))+","
            s2+=i
        s1=s1[:-1]
        return s1+'#'+s2

    def decode(self, s: str) -> List[str]:
        if s=='#':
            return []
        for i in range(len(s)):
            if s[i] == '#':
                l=list((s[:i]).split(','))
                s1=s[i+1:]
                break
        r=[]
        x=0
        y=0
        i=0
        for i in range(len(l)):
            y=x+int(l[i])
            r.append(s1[x:y])
            x=y
        return r
