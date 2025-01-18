# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        while queue:
            ans = 0
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

        # dict={}
        # def dfs(node,level):
        #     if node is None:
        #         return
        #     if level not in dict:
        #         dict[level]=node.val
        #     else:
        #         dict[level]+=node.val
        #     dfs(node.left,level+1)
        #     dfs(node.right,level+1)
        # dfs(root, 0)
        # return dict[max(dict.keys())]

