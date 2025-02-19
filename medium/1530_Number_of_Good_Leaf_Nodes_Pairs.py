from turtle import left
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        ans = 0
        def dfs(node):
          nonlocal ans
          if not node:
            return []
          if not node.left and not node.right:
            return [1]
          left=dfs(node.left)
          right=dfs(node.right)
          for l in left:
            for r in right:
              if l+r<=distance:
                ans+=1

          merged = [i+1 for i in left+right if i+1 < distance]
          return merged
        dfs(root)
        return ans