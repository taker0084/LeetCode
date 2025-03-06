from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preOrder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #preOrderが空の場合
        if not preOrder:
            return
        #部分木のrootを取り出す
        root = TreeNode(preOrder[0])
        #preOrderが一つの場合、それが葉ノード
        if len(preOrder) == 1:
          return root
        #左部分木のルート
        left_root = preOrder[1]
        #左部分木のサイズ
        left_size = postorder.index(left_root) + 1
        root.left = self.constructFromPrePost(preOrder[1:left_size+1], postorder[:left_size])
        root.right = self.constructFromPrePost(preOrder[left_size+1:], postorder[left_size:-1])
        return root

preOrder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]