# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBst(node, lb, ub):
            if not node:
                return True
            
            if node.val <= lb or node.val >= ub:
                return False
            
            return _isValidBst(node.left, lb, node.val) and _isValidBst(node.right, node.val, ub)
        
        return _isValidBst(root, -1001, 1001)