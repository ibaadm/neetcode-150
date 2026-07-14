# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        serialized = []

        q = deque([root])
        while q:
            node = q.popleft()
            
            if node:
                serialized.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                serialized.append("N")

        while serialized[-1] == "N":
            serialized.pop()
        
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        serialized = data.split(",")
        root = TreeNode(int(serialized[0]))
        parents = deque([root])
        i = 1
        is_first_child = True
        while i < len(serialized):
            if is_first_child:
                parent = parents.popleft()
                if serialized[i] != "N":
                    parent.left = TreeNode(int(serialized[i]))
                    parents.append(parent.left)
            else:
                if serialized[i] != "N":
                    parent.right = TreeNode(int(serialized[i]))
                    parents.append(parent.right)
            i += 1
            is_first_child = not is_first_child
        return root