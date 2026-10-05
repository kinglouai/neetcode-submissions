class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t=[]
        for i in range(len(speed)):
            t.append((position[i],speed[i]))
        t.sort(reverse=True)
        p=[((target-t[0][0])/t[0][1])]
        for i in range(1,len(speed)):
            time=(target-t[i][0])/t[i][1]
            if time >p[-1]:
                 p.append(time)
        return len(p)
