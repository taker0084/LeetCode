from typing import Optional

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      """
      sumNumbers returns sum of all paths

      Args:
          root (Optional[TreeNode]): _description_

      Returns:
          int: _description_
      """
      if not root:
        return 0
      def dfs(node):
        if not node:
          return ""
        left = dfs(node.left)
        right = dfs(node.right)
        return self.add_value_to_path(node, left+right)
      path_list = dfs(root)
      total = 0
      for path in path_list:
        total += int(path)
      return total

    def add_value_to_path(self, node, path_list):
      """
      add_value_to_path adds value to all path in routes

      Args:
          node (_type_): _description_
          path_list (_type_): _description_

      Returns:
          _type_: _description_
      """
      if not path_list:
        return [str(node.val)]
      new_path_list = []
      for path in path_list:
        new_path_list.append(str(node.val) + path)
      return new_path_list
#--------TEST CASES----
@pytest.fixture
def solution():
  return Solution()

def test_sumNumbers(solution):
  #example1
  root = TreeNode(1, TreeNode(2), TreeNode(3))
  assert solution.sumNumbers(root) == 25
  #example2
  root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
  assert solution.sumNumbers(root) == 1026
