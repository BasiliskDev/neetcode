class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if (len(pq) >= k):
                if (pq[0] < num):
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)
            else:
                heapq.heappush(pq, num)
        return pq[0]
        