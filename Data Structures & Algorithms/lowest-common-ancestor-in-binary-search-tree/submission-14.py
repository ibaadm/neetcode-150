# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        found = 0
        paths = []
        def dfs(node, path):
            nonlocal found
            if not node or found == 2:
                return
            path.append(node)
            if node.val == p.val or node.val == q.val:
                paths.append(path[:])
                found += 1
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        i = 1
        n = min(len(paths[0]), len(paths[1]))
        while i < n and paths[0][i] == paths[1][i]:
            i += 1
        return paths[0][i-1]