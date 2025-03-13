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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        maxLevelSum returns minimum level of tree that has min sum

        Args:
            root (Optional[TreeNode]): root node of tree

        Returns:
            int: minimum number of level which has minimum sum of value
        """
        if not root:
          return 0
        queue_current_level = collections.deque([root])
        self.max_sum = 0
        self.max_sum_level = 0
        current_level = 0
        while queue_current_level:
          sum_of_level = 0
          current_level += 1
          for _ in range(len(queue_current_level)):
            current_node = queue_current_level.popleft()
            sum_of_level += current_node.val
            if current_node.left:
              queue_current_level.append(current_node.left)
            if current_node.right:
              queue_current_level.append(current_node.right)
          self.is_max_sum(current_level, sum_of_level)
        return self.max_sum_level

    def is_max_sum(self, sum_level, max_sum):
        """
        is_max_sum checks if current level's sum is greater than max sum

        Args:
            sum_level (_type_): current level
            max_sum (_type_): sum of current level's nodes
        """
        if max_sum > self.max_sum:
          self.max_sum = max_sum
          self.max_sum_level = sum_level
#----------TEST CASES----------#
@pytest.fixture
def solution():
  return Solution()

def test_max_level_sum(solution):
  #example1
  root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
  assert solution.maxLevelSum(root) == 2
  #example2
  root = TreeNode(989, TreeNode(10250, TreeNode(98693), TreeNode(-89388, TreeNode(-32127))))
  assert solution.maxLevelSum(root) == 2