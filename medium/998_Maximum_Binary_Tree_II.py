from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
          return None
        if val > root.val:
            return TreeNode(val, root, None)
        def dfs(node):
          if not node:
            return[]
          left = dfs(node.left)
          right = dfs(node.right)
          return left + [node.val] + right
        nodeList = dfs(root)
        nodeList.append(val)
        def makeTree(nodeList):
          if not nodeList:
            return
          root = TreeNode(max(nodeList))
          rootIndex = nodeList.index(root.val)
          root.left = makeTree(nodeList[:rootIndex])
          root.right = makeTree(nodeList[rootIndex+1:])
          return root
        return makeTree(nodeList)
