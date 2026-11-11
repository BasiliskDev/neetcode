class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(point) for point in points]
        adj_list = {}
        for point1 in points:
            for point2 in points:
                if (point1 == point2):
                    continue
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                adj_list[point1] = adj_list.get(point1, [])
                adj_list[point1].append([distance, point2])
        if not adj_list:
            return 0
        pq = [(0, points[0])]
        min_t = 0
        visited = set()
        while (len(pq)):
            recent = heapq.heappop(pq)
            if recent[1] in visited:
                continue
            visited.add(recent[1])
            min_t += recent[0]
            for distance, point in adj_list[recent[1]]:
                heapq.heappush(pq, (distance, point))
        return min_t if len(visited) == len(points) else 0
        