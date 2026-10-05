class MinStack:

    def __init__(self):
        self.l=[]
        self.m=9999999999999999

    def push(self, val: int) -> None:
        self.l.append(val)
        if val<self.m:
            self.m=val

    def pop(self) -> None:
        if self.l.pop()==self.m and len(self.l)>0:
            self.m=min(self.l)
        if len(self.l)<=0:
            self.m=999999999999999
        

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.m
