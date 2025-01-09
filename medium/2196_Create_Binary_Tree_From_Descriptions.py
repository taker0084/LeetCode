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
        children=set()
        for description in descriptions:
            if description[0] not in num_dict:
                num_dict[description[0]] = TreeNode(description[0])
            if description[1] not in num_dict:
                num_dict[description[1]] = TreeNode(description[1])

            if description[2]:
                num_dict[description[0]].left = num_dict[description[1]]
            else:
                num_dict[description[0]].right = num_dict[description[1]]
            children.add(description[1])
        for num in num_dict:
            if num not in children:
                return num_dict[num]
        return None