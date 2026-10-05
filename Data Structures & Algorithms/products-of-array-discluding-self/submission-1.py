class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        c=0
        x=0
        for i in nums:
            if i!=0:
                p*=i
            else:
                c+=1
        if c>1:
            return [0]*len(nums)
        elif c==1:
            l=[0]*len(nums)
            for i in range(len(nums)):
                if nums[i]==0:
                    l[i]=p
            return l
        else:
            l=[0]*len(nums)
            for i in range(len(nums)):
                l[i]=int(p/nums[i])
            return l
