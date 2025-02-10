from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stringValue = '0'
        ans = 0
        def dfs(node,stringValue):
          nonlocal ans
          stringValue += str(node.val)
          #子がいない場合
          if not node.left and not node.right:
            print(stringValue)
            ans += int(stringValue,2)
          #左部分木について探索
          if node.left:
            dfs(node.left, stringValue)
          #右部分木について探索
          if node.right:
            dfs(node.right,stringValue)
        dfs(root,stringValue)
        return ans