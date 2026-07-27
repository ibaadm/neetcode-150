class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        
        visited = [False] * numCourses
        visiting = [False] * numCourses

        def dfs(u):
            visiting[u] = True
            res = False
            for v in adjList[u]:
                if visited[v]:
                    continue
                if visiting[v]:
                    return True
                res = res or dfs(v)
            visiting[u] = False
            visited[u] = True
            return res

        for u in range(numCourses):
            if not visited[u]:
                if dfs(u):
                    return False
        return True