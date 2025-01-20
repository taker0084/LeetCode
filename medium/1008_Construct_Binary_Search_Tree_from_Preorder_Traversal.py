# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreOrder(self, preOrder: List[int]) -> Optional[TreeNode]:
        # def dfs(node, val):
        #     if not node:
        #         return TreeNode(val)
        #     if val < node.val:
        #         node.left = dfs(node.left, val)
        #     else:
        #         node.right = dfs(node.right, val)
        #     return node
        # root = TreeNode(preorder[0])
        # for i in range(1,len(preorder)):
        #     dfs(root, preorder[i])
        # return root
        
        
        root = TreeNode(preOrder[0])
        for i in range(1, len(preOrder)):
            node = TreeNode(preOrder[i])
            cur = root
            while True:
                if node.val < cur.val:
                    if cur.left is None:
                        cur.left = node
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
        return root