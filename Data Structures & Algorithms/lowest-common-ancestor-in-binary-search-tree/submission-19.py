# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lb = -100
        ub = 100
        while root:
            if q.val == root.val:
                return root
            if p.val < root.val:
                ub = root.val
                if q.val < lb or q.val > ub:
                    return root
                root = root.left
            elif p.val > root.val:
                lb = root.val
                if q.val < lb or q.val > ub:
                    return root
                root = root.right
            else:
                return root

            