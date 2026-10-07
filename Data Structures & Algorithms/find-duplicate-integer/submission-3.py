class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=nums[0]
        y=nums[nums[0]]
        while x!=y:
            x=nums[x]
            y=nums[nums[y]]
        z=0
        while x!=z:
            x=nums[x]
            z=nums[z]
        return x
            