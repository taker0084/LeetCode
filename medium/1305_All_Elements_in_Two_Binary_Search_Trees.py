# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root1)
        dfs(root2)
        return sorted(ans)
