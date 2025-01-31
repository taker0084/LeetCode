# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.dfs(root)

    def dfs(self, node):
        while node:
            self.stack.append(node.val)
            self.dfs(node.left)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.dfs(node.right)
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()