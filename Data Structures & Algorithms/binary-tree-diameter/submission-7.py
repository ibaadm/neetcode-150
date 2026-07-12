# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def _diameterOfBinaryTree(node):
            if not node:
                return (0, 0)
            
            left_diam, left_depth = _diameterOfBinaryTree(node.left)
            right_diam, right_depth = _diameterOfBinaryTree(node.right)
            diameter = max(left_diam, right_diam, left_depth + right_depth)
            return (diameter, max(left_depth, right_depth) + 1)

        return _diameterOfBinaryTree(root)[0]