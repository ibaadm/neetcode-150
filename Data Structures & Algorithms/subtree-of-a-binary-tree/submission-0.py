# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        def sameTree(p, q):
            if not p:
                return not q
            if not q:
                return not p
            return sameTree(p.left, q.left) and sameTree(p.right, q.right) and p.val == q.val
        
        return dfs(root)