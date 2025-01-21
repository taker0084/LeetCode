# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)
        return dfs(root)

        #遅かったので不採用
        # match node.val:
        #     case 0:
        #         return False
        #     case 1:
        #         return True
        #     case 2:
        #         return self.evaluateTree(node.left) or self.evaluateTree(node.right)
        #     case 3:
        #         return self.evaluateTree(node.left) and self.evaluateTree(node.right)