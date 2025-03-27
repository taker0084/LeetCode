import collections
from typing import List, Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        current_level_nodes = collections.deque([root])
        result = []
        while current_level_nodes:
            current_nodes_val = []
            for _ in range(len(current_level_nodes)):
                node = current_level_nodes.popleft()
                current_nodes_val.append(node.val)
                if node.left:
                    current_level_nodes.append(node.left)
                if node.right:
                    current_level_nodes.append(node.right)
            result.append(current_nodes_val[-1])
        return result
#------------TEST CASES----------------
@pytest.fixture
def root():
    return TreeNode()

def test_rightSideView():
    """
    Example1: normal tree case
    Example2: no root
    """
    #Example1
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    solution = Solution()
    assert solution.rightSideView(root) == [1,3,4]
    # Example2
    root = None
    assert solution.rightSideView(root) == []