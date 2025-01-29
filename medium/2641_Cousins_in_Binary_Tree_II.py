# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root.val = 0
        # sumDepth=[0]
        # def dfs(node,depth):
        #     if not node:
        #         return
        #     sum[depth] += node.val
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        # dfs(root, 0)
        # def dfs2(node, depth):
        #     if not node:
        #         return
        #     if node.left and node.right:
        #         node.left.val = sum[depth + 1] - node.left.val - node.right.val
        #     elif node.left:
        #         node.left.val = sum[depth + 1] - node.left.val
        #     elif node.right:
        #         node.right.val = sum[depth + 1] - node.right.val
        #     dfs2(node.left, depth + 1)
        #     dfs2(node.right, depth + 1)
        # dfs2(root, 0)
        root.val = 0
        #qは次の深さのNodeを管理
        q = [root]
        while q:
            #tmpは現在の深さのノード
            tmp = q
            q = []

            #次の深さでのnodeの合計
            next_level_sum = 0
            #次の深さでの合計値を計算
            for node in tmp:
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val
            
            #現在の深さのノードに関して以下を計算
            for node in tmp:
                #そのノードの子ノードの合計
                children_sum = 0
                if node.left:
                    children_sum += node.left.val
                if node.right:
                    children_sum += node.right.val
                #計算したnodeの合計値を深さの合計値からひく
                if node.left:
                    node.left.val = next_level_sum - children_sum
                if node.right:
                    node.right.val = next_level_sum - children_sum
        return root