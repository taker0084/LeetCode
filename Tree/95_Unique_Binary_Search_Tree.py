# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
      result=[]
      input=[i for i in range(1,n+1)]
      if n==0:
        return result
      def dfs(node):
        if node is None:
          return
        dfs(node.left)
        dfs(node.right)
      for i in range(1,n):
        root=TreeNode(i)
        dfs(root)