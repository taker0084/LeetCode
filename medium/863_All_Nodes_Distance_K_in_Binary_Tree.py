from turtle import right
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
          return
        ans = []
        def dfs(node):
          if not node.left or node.right:
            return [node.val, 1]
          left = dfs(node.left)
          right = dfs(node.right)
          