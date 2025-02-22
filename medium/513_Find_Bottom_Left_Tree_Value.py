from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
          return None
        cur = deque([root])
        next = deque([root])
        cur = next
        while cur:
          curLen = len(cur)
          leftmost = cur[0].val
          for _ in range(curLen):
            node = cur.popleft()
            if node.right:
              next.append(node.right)
            if node.left:
              next.append(node.left)
          if len(next) == 0:
            return leftmost
          cur = next