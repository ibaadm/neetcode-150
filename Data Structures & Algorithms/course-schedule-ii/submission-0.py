class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses
        for v, u in prerequisites:
            adjList[u].append(v)
            in_deg[v] += 1
        
        q = deque([u for u in range(numCourses) if in_deg[u] == 0])
        topological = []
        while q:
            u = q.popleft()
            topological.append(u)
            for v in adjList[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        
        return topological if len(topological) == numCourses else []