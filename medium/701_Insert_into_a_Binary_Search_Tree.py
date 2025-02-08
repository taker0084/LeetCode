from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        New = TreeNode(val)
        def dfs(node):
          if not node:
            root = New
            return
          if node.val > val:
            if node.left:
              dfs(node.left)
            else:
              node.left = New
          else:
            if node.right:
              dfs(node.right)
            else:
              node.right = New
          return root
        return dfs(root)