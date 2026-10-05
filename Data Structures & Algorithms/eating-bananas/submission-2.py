import math
class Solution:
    def minEatingSpeed(self, piles: pilest[int], h: int) -> int:
        l=1
        r=max(piles)
        k=r
        while l<=r:
            m=(l+r)//2
            t=0
            for i in range(len(piles)):
                t+=math.ceil(piles[i]/m)
            if t>h:
                l=m+1
            else:
                k=min(k,m)
                r=m-1
        return k



        