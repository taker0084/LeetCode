"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        cur = deque([root])
        ans = []
        next = deque([root])
        cur = next
        while cur:
          level = []
          qLen = len(cur)
          for _ in range(qLen):
            node = cur.popleft()
            level.append(node.val)
            if node.children:
              for child in node.children:
                next.append(child)
          ans.append(level)
          cur = next
        return ans