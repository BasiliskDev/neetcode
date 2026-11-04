class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]
        ls = [(0, k)]
        visited = set()
        for source, dest, weight in times:
            adj_list[source].append([weight, dest])
        t=0
        while ls:
            curr_dist, currnode = heapq.heappop(ls)
            if currnode in visited:
                continue
            visited.add(currnode)
            t=curr_dist
            
            for dist, next_node in adj_list[currnode]:
                if next_node not in visited:
                    heapq.heappush(ls, (curr_dist + dist, next_node))

            
        return t if len(visited) == n else -1




        

        

        