class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=dict()
        x=0
        y=0
        c=0
        m=0
        while y<len(s):
            if s[y] in d:
                d.pop(s[x], None)
                x+=1
                c-=1
            else:
                d[s[y]]=1
                c+=1
                y+=1
                m=max(m,c)
        return m
