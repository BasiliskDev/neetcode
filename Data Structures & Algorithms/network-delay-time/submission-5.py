class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n+1)]
        for source, target, time in times:
            adj_list[source].append([target, time])
        pq = []
        heapq.heappush(pq, (0, k))
        visited = set()
        max_time = 0
        while (len(pq)):
            recent = heapq.heappop(pq)
            if recent[1] in visited:
                continue
            max_time = recent[0]
            visited.add(recent[1])
            for node, time in adj_list[recent[1]]:
                heapq.heappush(pq, (recent[0] + time, node))
            #print(pq)
        
        return max_time if len(visited) == n else -1


        

        

        