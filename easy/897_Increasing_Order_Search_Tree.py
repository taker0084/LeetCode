# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #初期rootを仮としておく
        root_min=TreeNode()
        #現在位置
        cur=root_min
        def dfs(node):
            nonlocal cur
            if not node:
                return
            #左部分木を探索
            dfs(node.left)
            #現在位置のノードの右につける
            cur.right=TreeNode(node.val)
            #現在位置を更新
            cur=cur.right
            #右部分木を探索
            dfs(node.right)
        dfs(root)

        return root_min.right
