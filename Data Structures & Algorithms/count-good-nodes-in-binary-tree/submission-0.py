# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def _goodNodes(node, curr_max):
            if not node:
                return 0
            is_good = node.val >= curr_max
            curr_max = max(curr_max, node.val)
            return is_good + _goodNodes(node.left, curr_max) + _goodNodes(node.right, curr_max)
        return _goodNodes(root, -100)