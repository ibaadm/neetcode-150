# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        mp = {None: 0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                stack.pop()
                left_depth = mp[node.left]
                right_depth = mp[node.right]
                if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                    mp[node] = -1
                else:
                    mp[node] = max(left_depth, right_depth) + 1
        return mp[root] != -1