# Definition for a binary tree node.
from re import A
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        isRange = lambda x: low <= x <= high
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            if isRange(node.val):
                ans += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val<low:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return ans

root = [10,5,15,3,7,None,18]
low = 7
high = 15
print(Solution().rangeSumBST(root,low,high))