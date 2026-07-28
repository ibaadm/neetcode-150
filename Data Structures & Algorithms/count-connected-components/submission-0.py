class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(u):
            visited.add(u)
            for v in adjList[u]:
                if v not in visited:
                    dfs(v)
        
        visited = set()
        numComponents = 0
        for u in range(n):
            if u not in visited:
                dfs(u)
                numComponents += 1
        return numComponents