# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mp = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def _buildTree(l, r):
            nonlocal pre_idx
            if r < l: return None

            root = TreeNode(preorder[pre_idx])
            split = mp[root.val]
            pre_idx += 1
            root.left = _buildTree(l, split-1)
            root.right = _buildTree(split+1, r)
            return root

        return _buildTree(0, len(inorder)-1)
        """
        inorder is left root right
        preorder is root left right
        if tree is [1, 2, 3, 4, 5, 6, 7]
        preorder is [1, 2, 4, 5, 3, 6, 7]
        inorder is [4, 2, 5, 1, 6, 3, 7]
        implementation:
        create the current node
        build the left subtree and attach
        build the right subtree and attach
        """