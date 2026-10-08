class LRUCache:

    def __init__(self, capacity: int):
        self.d=dict()
        self.c=capacity 
        self.l=[]
    def get(self, key: int) -> int:
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key]=value
            self.l.remove(key)
            self.l.append(key)
        else:
            if self.c>0:
                self.d[key]=value
                self.c-=1
                self.l.append(key)
            else:
                self.d.pop(self.l[0])
                self.l.remove(self.l[0])
                self.d[key]=value
                self.l.append(key)


    
        
