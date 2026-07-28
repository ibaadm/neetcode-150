class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        size = [1] * (n+1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if size[px] < size[py]:
                px, py = py, px
            size[px] += size[py]
            parent[py] = px
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        