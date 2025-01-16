# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,level):
            if not node:
                return
            if level%2==1 and node.left and node.right:
                node.left.val,node.right.val = node.right.val,node.left.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return root

