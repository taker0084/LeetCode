from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
          return None
        def dfs(node):
          if not node:
            if not node:
              return 0, None
          #左部分木
          left_depth, left_node = dfs(node.left)
          #右部分木
          right_depth, right_node = dfs(node.right)
          #左部分木が深い場合、左のノードを返す
          if left_depth > right_depth:
            return left_depth + 1, left_node
          #右も同様
          elif left_depth < right_depth:
            return right_depth + 1, right_node
          #両方同じ場合、自分を返す
          else:
            return left_depth, node
        _,node = dfs(root)
        return node