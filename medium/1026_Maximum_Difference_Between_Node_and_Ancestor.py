# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        min_value=max_value=root.val
        def dfs(node,min_value,max_value):
            if not node:
                return max_value-min_value
            min_value=min(node.val,min_value)
            max_value=max(node.val,max_value)
            return max(dfs(node.left,min_value,max_value),dfs(node.right,min_value, max_value))
        return dfs(root,min_value, max_value)