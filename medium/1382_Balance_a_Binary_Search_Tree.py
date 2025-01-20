# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #全ノードを列挙
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node] + dfs(node.right)
        #全ノードのリスト作成
        nodeList = dfs(root)
        #新たに木を作成
        def buildBST(nodeList):
            if not nodeList:
                return None
            mid = len(nodeList) // 2
            node = nodeList[mid]
            node.left = buildBST(nodeList[:mid])
            node.right = buildBST(nodeList[mid+1:])
            return node
        return buildBST(nodeList)