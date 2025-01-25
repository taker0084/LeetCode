# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.dict={}
        self.root=root
        def dfs(node,level):
            if node is None:
                return
            self.dict[level]=node.val
            dfs(node.left,level*2+1)
            dfs(node.right, level*2+2)
        dfs(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.dict.values()


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)