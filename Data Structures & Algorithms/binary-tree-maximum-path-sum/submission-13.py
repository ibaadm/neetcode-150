# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def _maxPathSum(node):
            if not node:
                return 0

            nonlocal res
            
            left = _maxPathSum(node.left)
            right = _maxPathSum(node.right)

            curr = max(
                left + node.val,
                right + node.val,
                node.val
            )
            res = max(res, curr, left + right + node.val)
            return curr

        _maxPathSum(root)
        return res