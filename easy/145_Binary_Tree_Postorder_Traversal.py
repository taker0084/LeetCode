# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodeList = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            nodeList.append(node.val)
        return nodeList