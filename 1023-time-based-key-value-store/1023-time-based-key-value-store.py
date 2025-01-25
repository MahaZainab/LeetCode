class TimeMap:

    def __init__(self):
        self.Store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Store:
            self.Store[key]=[]
        self.Store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.Store.get(key, [])
        first, last= 0, len(values)-1
        while first<=last:
            mid=(first+last)//2
            if values[mid][1]<=timestamp:
                res=values[mid][0]
                first=mid+1
            else:
                last=mid-1
        return res
        
