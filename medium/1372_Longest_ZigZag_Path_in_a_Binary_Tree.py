from typing import Optional

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        longestZigZag returns the longest zigzag route

        Args:
            root (Optional[TreeNode]): a route of tree

        Returns:
            int: the number of longest zigzag routes
        """
        if not root:
          return 0
        def dfs(node: Optional[TreeNode], is_left: bool, length: int) -> int:
            if not node:
                return length
            if is_left:
              return max(dfs(node.right, False, length + 1), dfs(node.left, True, 1))
            return max(dfs(node.left, True, length + 1), dfs(node.right, False, 1))
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
#----------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()
def test_longestZigZag(solution):
    """
    Test case 1: Normal Tree Structure
    Test case 2: No root
    """
    # Example1
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert solution.longestZigZag(root) == 2
    # Example2
    root = None
    assert solution.longestZigZag(root) == 0