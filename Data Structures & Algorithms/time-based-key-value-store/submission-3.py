class TimeMap:

    def __init__(self):
        self.d=dict()
        self.l=[]
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key,timestamp)]=value
        self.l.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not self.l:
            return ""
            
        l = 0
        r = len(self.l) - 1
        best_idx = -1
        
        while l <= r:
            m = (l + r) // 2
            if self.l[m] <= timestamp:
                best_idx = m
                l = m + 1
            else:
                r = m - 1
                

        while best_idx >= 0:
            ts = self.l[best_idx]
            if (key, ts) in self.d:
                return self.d[(key, ts)]
            best_idx -= 1
            
        return ""
        
      
        
