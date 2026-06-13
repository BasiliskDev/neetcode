class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False for _ in range(len(edges)+1)]
        cycle = set()
        cycleStart = -1

        def dfs(pos, prev):
            nonlocal cycleStart
            if (visited[pos]):
                cycleStart = pos
                return True
            
            visited[pos] = True
            for node in adj_list[pos]:
                if (node == prev):
                    continue
                if (dfs(node, pos)):
                    if cycleStart != -1:
                        cycle.add(pos)
                    if pos == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1,-1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
    

        