class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mi=99999999
        while l<=r:
            m=(l+r)//2
            mi=min(mi,nums[m])
            print(mi)
            if nums[r]<nums[l] and nums[m]>nums[r]:
                l=m+1
            else:
                r=m-1
        return mi