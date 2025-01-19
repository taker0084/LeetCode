# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            ans = 0
            if grandparent and grandparent.val % 2 == 0:
                ans += node.val
            ans += dfs(node.left, node, parent)
            ans += dfs(node.right, node, parent)
            return ans
        return dfs(root, None, None)
