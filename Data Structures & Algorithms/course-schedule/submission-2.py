class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_taken = [False] * numCourses
        visited = [False] * numCourses

        adj_list = [[] for _ in range(numCourses)]

        for p in prerequisites:
            adj_list[p[0]].append(p[1])

        print(adj_list)
        contradiction = False
        
        def dfs(course):
            nonlocal adj_list, contradiction
            if (contradiction):
                return
            visited[course] = True
            for pre in adj_list[course]:
                if (not course_taken[pre]):
                    if (visited[pre]):
                        contradiction = True
                    dfs(pre)
            course_taken[course] = True

        for i in range(len(adj_list)):
            dfs(i)
            if (contradiction):
                return False

        return True
        