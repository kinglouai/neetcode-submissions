class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]<=target and matrix[m][-1]>=target:
                l1=0
                r1=len(matrix[m])-1
                while l1<=r1:
                    m1=(l1+r1)//2
                    if matrix[m][m1]==target:
                        return True
                    elif  matrix[m][m1]<target:
                        l1=m1+1
                    else:
                        r1=m1-1

                return False
            elif matrix[m][-1]<target:
                l=m+1
            else:
                r=m-1
        return False
            
        