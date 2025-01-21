from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        num_dict = {}
        root = None
        for _,k,_ in descriptions:
            num_dict[k] = TreeNode(k)

        for p,_,_ in descriptions:
            if p not in num_dict:
                root = TreeNode(p)
                num_dict[p] = root

        for p,k,side in descriptions:
            if side:
                num_dict[p].left = num_dict[k]
            else:
                num_dict[p].right = num_dict[k]
        return root