from collections import deque
from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self._ans = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
          return []
        ans = []
        cur = deque([root])
        while cur:
          level = self.BFS(cur)
          cur = next
        return self._ans

    def BFS(self, current:deque[TreeNode]) -> List[int]:
      level = []
      next = deque()
      curLen=len(current)
      for _ in range(curLen):
        node = current.popleft()
        level.append(node.val)
        if node.left:
          next.append(node.left)
        if node.right:
          next.append(node.right)
      self._ans.append(level)
      return level