class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w=0
        x=0
        y=len(heights)-1
        while x<y:
            w=max(w,min(heights[x],heights[y])*(y-x))
            if heights[x]<heights[y]:
                x+=1
            else:
                y-=1
        return w
