class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        p=[(0,heights[0])]
        a=0
        for i in range(1,len(heights)):
            start=i
            while p and heights[i]<=p[-1][1]:
                x=p.pop()
                a=max(a,(x[1])*(i-x[0]))
                start=x[0]
            p.append((start,heights[i]))

        for i in range(len(p)):
            a=max(a,(len(heights)-p[i][0])*p[i][1])
        return a

                


        