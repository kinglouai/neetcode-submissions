class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict() 
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=sorted(d, key=d.get, reverse=True)
        ll=l[:k]
        return ll

                