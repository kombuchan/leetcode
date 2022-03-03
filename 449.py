# Serialize and Deserialize BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:
    
    def preorder_traversal(self, node, s):
        if node == None: 
            s.append('-1')
            return 0
        else: s.append(str(node.val))
        self.preorder_traversal(node.left,s)
        self.preorder_traversal(node.right,s)
        
        return s

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root == None: return ""
        return (",".join(self.preorder_traversal(root,[])))
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "" : return []
        data = [int(i) for i in data.split(',')]
        data = deque(data)
        
        return self.buildTree(data)
        
        
    def buildTree(self,data):
        val = data.popleft()
        if val == -1: return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        
        return node


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
