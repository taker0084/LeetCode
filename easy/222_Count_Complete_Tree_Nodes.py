from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count
        return self.dfs(root, count)

    def dfs(self,node,count):
        count += 1
        if node.left:
            self.dfs(node.left,count)
        if node.right:
            self.dfs(node.right,count)
        return count