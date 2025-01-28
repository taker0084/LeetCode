# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            if not node:
                return 0
            #左から移動するコインの合計
            left = dfs(node.left)
            #右から移動するコインの合計
            right = dfs(node.right)
            #累計で移動させるコイン
            ans += abs(left) + abs(right)
            #合計で移動させるコイン数
            return node.val + left + right - 1
        dfs(root)
        return ans