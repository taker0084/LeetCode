from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
          if not root: 
            return 0, None
          #左部分木の高さとLCA
          h1, lca1 = dfs(root.left)
          #右部分木の高さとLCA
          h2, lca2 = dfs(root.right)
          
          if h1 > h2: return h1 + 1, lca1
          if h1 < h2: return h2 + 1, lca2
          return h1 + 1, root
        return dfs(root)[1]