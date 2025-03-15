import collections
from typing import Optional

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        isEvenOddTree:
          if level(depth) is even number -> values are even and descending order

          else -> values are odd and ascending order

        Args:
            root (Optional[TreeNode]): a root of tree

        Returns:
            bool: is given tree is even-odd-tree?
        """
        if not root:
          return False
        current_level_nodes=collections.deque([root])
        is_even = True
        ans = True
        while current_level_nodes:
          current_level_values=[]
          last_node = 0 if is_even else 10**6+1
          for _ in range(len(current_level_nodes)):
            current_node=current_level_nodes.popleft()
            if is_even:
              if current_node.val%2 == 0 or current_node.val <= last_node:
                return False
              last_node = current_node.val
            else:
              if current_node.val%2 != 0 or current_node.val >= last_node:
                return False
              last_node = current_node.val

            current_level_values.append(current_node.val)
            if current_node.left:
              current_level_nodes.append(current_node.left)
            if current_node.right:
              current_level_nodes.append(current_node.right)
          is_even = not is_even
        return ans
#---------TEST--------------------------
@pytest.fixture
def solution():
  return Solution()

def test_isEvenOddTree(solution):
    """
    Example1: normal True case
    Example2: normal False case
    Example3: if root is none

    """
    #Example1
    root = TreeNode(1,TreeNode(10,TreeNode(3)),TreeNode(4,TreeNode(7),TreeNode(9)))
    assert solution.isEvenOddTree(root) == True
    #Example2
    root = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(7)))
    assert solution.isEvenOddTree(root) == False
    # Example3
    root = None
    assert solution.isEvenOddTree(root) == False