# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node, height):
        if node == None:
            return float("inf")
        
        if node.left == None and node.right == None:
            return height
        
        return min(self.recurse(node.left, height+1), self.recurse(node.right, height+1))
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.recurse(root, 1)