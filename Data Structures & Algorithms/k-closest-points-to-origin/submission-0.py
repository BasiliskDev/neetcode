class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for idx, point in enumerate(points):
            heapq.heappush(pq, (math.sqrt(point[0]**2 + point[1]**2), idx))
        
        return [points[i[1]] for i in heapq.nsmallest(k, pq)]

        