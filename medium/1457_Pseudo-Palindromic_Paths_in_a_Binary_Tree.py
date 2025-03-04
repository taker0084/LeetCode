from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = deque([(root, 0)])

        while queue:
            node, path = queue.popleft()

            if node:
                # 含まれている値を調べる(含まれているビットが1になっている)
                # ^= は XORであるため、2回出てくると0に戻る
                path ^= 1 << node.val

                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    queue.append((node.left, path))
                    queue.append((node.right, path))

        return count