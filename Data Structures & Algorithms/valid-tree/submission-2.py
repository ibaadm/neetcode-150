class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False

        parent = list(range(n))
        size = [1] * n

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
                return False
        return True