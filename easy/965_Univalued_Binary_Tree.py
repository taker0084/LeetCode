from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
          return True
        val = root.val
        def dfs(node):
          if not node:
            return True
          if node.val != val:
            return False
          left = dfs(node.left)
          right = dfs(node.right)
          return left & right
        return dfs(root)