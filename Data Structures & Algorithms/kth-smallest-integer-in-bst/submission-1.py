# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        res = self.kthSmallest(root.left, k)
        if res != -1:
            return res
        self.count += 1
        if self.count == k:
            return root.val
        return self.kthSmallest(root.right, k)