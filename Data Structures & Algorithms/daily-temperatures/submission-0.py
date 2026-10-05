class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        p=[0]
        l=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            if temperatures[i]<temperatures[p[-1]]:
                p.append(i)
            else:
                while len(p)>0 and temperatures[i]>temperatures[p[-1]]:
                    x=p.pop()
                    l[x]=i-x
                p.append(i)
        return l

