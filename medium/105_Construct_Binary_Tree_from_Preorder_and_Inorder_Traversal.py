from typing import List, Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            mid_index = inorder.index(preorder[0])
            root.left = dfs(preorder[1:mid_index+1], inorder[:mid_index])
            root.right = dfs(preorder[mid_index+1:], inorder[mid_index+1:])
            return root
        return dfs(preorder, inorder)
#----------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_buildTree(solution):
    """
    Test case 1: Normal Tree Structure
    Test case 2: No root
    """
    # Example1
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    assert solution.buildTree(preorder, inorder) == TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # Example2
    preorder = [-1]
    inorder = [-1]
    assert solution.buildTree(preorder, inorder) == TreeNode(-1)