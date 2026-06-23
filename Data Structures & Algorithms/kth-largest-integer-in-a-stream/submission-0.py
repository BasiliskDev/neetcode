class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        self.k = k
        heapq.heapify(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.pq, val)
        print(self.pq)
        return heapq.nlargest(self.k,self.pq)[-1]
        
