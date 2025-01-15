# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[]
        sum = 0
        def dfs(node):
            nonlocal sum  #外側のスコープの変数を使いたい場合
            if node:
                dfs(sum,node.right)
                sum += node.val
                node.val=sum
                dfs(sum,node.left)
        dfs(sum,root)
        return root

root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
print(Solution().bstToGst(root))