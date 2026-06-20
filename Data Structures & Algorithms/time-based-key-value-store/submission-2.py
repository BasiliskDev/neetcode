class TimeMap:

    def __init__(self):
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.times):
            self.times[key] = []
        self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        arr = self.times[key]
        if len(arr) == 0:
            return ""
        lo = 0
        hi = len(arr)-1
        decreased = False
        while (lo <= hi):
            mid = lo + (hi-lo)//2
            if (arr[mid][0] < timestamp):
                lo = mid+1
                decreased = True
            elif (arr[mid][0] > timestamp):
                hi = mid - 1
            else:
                return arr[mid][1]
        if (not decreased):
            return ""
        return arr[lo-1][1]


        
