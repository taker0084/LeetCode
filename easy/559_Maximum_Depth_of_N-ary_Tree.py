"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxDepth = 0
        def dfs(node,depth):
          nonlocal maxDepth
          if not node:
            return
          if depth > maxDepth:
            maxDepth = depth
          for child in node.children:
            dfs(child, depth+1)
        dfs(root,1)
        return maxDepth
