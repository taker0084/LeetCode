# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = max = -10**4
        def dfs(node,max):
          nonlocal ans
          if not node:
            return
          if node.val >= max:
            ans += 1
          dfs(node.left, node.val)
          dfs(node.right,node.val)
        dfs(root,max)
        return ans
