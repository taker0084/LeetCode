# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            qLen = len(q)
            valDepth=0
            for i in range(qLen):
              node = q.popleft()
              valDepth += node.val
              if node.left:
                q.append(node.left)
              if node.right:
                q.append(node.right)
            ans.append(valDepth/qLen)
        return ans