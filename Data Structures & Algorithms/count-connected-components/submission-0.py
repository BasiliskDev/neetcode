class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        print(adj_list)

        visited = [False for _ in range(n)]
        components = 0
        def dfs(pos):
            visited[pos] = True
            for node in adj_list[pos]:
                if (not visited[node]):
                    dfs(node)
        
        for i in range(len(visited)):
            if (not visited[i]):
                components += 1
                dfs(i)
        return components
        