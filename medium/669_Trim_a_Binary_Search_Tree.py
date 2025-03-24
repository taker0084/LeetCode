from typing import Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        trimBST() returns a trim binary search tree that all value of nodes are included in low to high

        Args:
            root (Optional[TreeNode]): a root of binary search tree
            low (int): a minimum value of tree
            high (int): a maximum value of tree

        Returns:
            Optional[TreeNode]: a root of trimBST
        """
        if not root:
            return None
        def dfs(node):
            if not node:
                return None
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
        dfs(root)
        return root
#----------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_trimBST(solution):
    """
    Test case 1: Normal Tree Structure
    Test case 2: No root
    """
    # Example1
    root = TreeNode(3, TreeNode(0, None, TreeNode(2)), TreeNode(4))
    low = 1
    high = 3
    assert solution.trimBST(root, low, high) == TreeNode(3, TreeNode(2),None)
    # Example2
    root = None
    low = 1
    high = 3
    assert solution.trimBST(root, low, high) == None
