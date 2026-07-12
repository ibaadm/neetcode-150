# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        keep a track of the deepest and the diameter of each subtree
        at each recursive step, check if using the deepest node of the left and the right would change anything
        if a root node gets added to a diameter, 2 edges are added? not always
        '''
        def _diameterOfBinaryTree(node):
            if not node:
                return (0, 0)
            
            left = _diameterOfBinaryTree(node.left)
            right = _diameterOfBinaryTree(node.right)
            diameter = max(left[0], right[0], left[1]+right[1])
            return (diameter, max(left[1], right[1]) + 1)

        return _diameterOfBinaryTree(root)[0]