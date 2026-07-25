"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        cloned = Node(node.val)
        stack = [(node, cloned)]
        visited = {node.val: cloned}

        while stack:
            orig_curr, cloned_curr = stack.pop()
            for neighbor in orig_curr.neighbors:
                if neighbor.val not in visited:
                    cloned_neighbor = Node(neighbor.val)
                    visited[neighbor.val] = cloned_neighbor
                    stack.append((neighbor, cloned_neighbor))
                cloned_curr.neighbors.append(visited[neighbor.val])
        
        return cloned
        