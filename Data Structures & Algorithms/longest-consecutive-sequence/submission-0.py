class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=dict()
        d1=dict()
        for i in range(len(nums)) :
            d[nums[i]]=i
        for i in range(len(nums)):
            if nums[i]-1 not in d :
                d1[nums[i]]=i
        m=0
        for i in d1:
            x=i+1
            c=1
            while x in d:
                c+=1
                x+=1
            if c>m:
                m=c
        return m