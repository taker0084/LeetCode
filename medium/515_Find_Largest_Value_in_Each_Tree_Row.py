from typing import List, Optional

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        returns a list of maximum values by tree level

        Args:
            root (Optional[TreeNode]): a root node of this tree

        Returns:
            List[int]: a list of maximum values by tree level
        """
        if not root:
            return []
        current_level_queue = [root]
        ans_list = []
        while current_level_queue:
            current_level_max = max(current_level_queue, key=lambda x: x.val)
            ans_list.append(current_level_max.val)
            for _ in range(len(current_level_queue)):
                node = current_level_queue.pop(0)
                if node.left:
                    current_level_queue.append(node.left)
                if node.right:
                    current_level_queue.append(node.right)
        return ans_list
#---------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()
def test_largestValues(solution):
    """
    Test case 1: Normal Tree Structure
    Test case 2: No root
    """
    # Example1
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert solution.largestValues(root) == [1, 3, 9]
    # Example2
    root = None
    assert solution.largestValues(root) == []