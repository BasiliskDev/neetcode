class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        ret = []
        adjList = [[] for _ in range(numCourses)]
        for course_pair in prerequisites:
            adjList[course_pair[0]].append(course_pair[1])
        
        def topoSort(node):
            if (node in cycle):
                return False
            if (node in visited):
                return True
            cycle.add(node)
            for new_node in adjList[node]:
                if not topoSort(new_node):
                    return False
            cycle.remove(node)
            ret.append(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not topoSort(i):
                return []
        
        return ret
        

        