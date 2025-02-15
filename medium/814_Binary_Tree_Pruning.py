from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
          if not node:
            return 0
          #左部分木が1を含むか
          left = dfs(node.left)
          #意を含まない場合、削除
          if not left:
            node.left = None
          right = dfs(node.right)
          if not right:
            node.right = None
          #その部分木が1を含むか
          return left + right + node.val > 0
        ans = dfs(root)
        if ans:
            return root
        else:
            return None