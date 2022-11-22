# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self, node, target, path):
        
        if node == None:
            return False
        
        if node.left == None and node.right == None:
            return path + node.val == target

        return self.findPath(node.left, target, path + node.val) or self.findPath(node.right, target, path + node.val)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.findPath(root, targetSum, 0)