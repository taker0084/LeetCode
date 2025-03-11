from turtle import left
from typing import Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
       self.node = None
    def flatten(self, root: Optional[TreeNode]) -> None:
      """
      flatten returns Linked list from root
      Do not return anything, modify root in-place instead.

      Args:
          root (Optional[TreeNode]): a root of tree
      """
      if not root:
        return
      self.flatten(root.right)
      self.flatten(root.left)

      root.right = self.node
      root.left = None
      self.node = root
#------Test CASES------
@pytest.fixture
def solution():
  return Solution()

def test_flatten(solution):
  root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
  solution.flatten(root)
  assert root.val == 1
  assert root.right.val == 2
  assert root.right.right.val == 3
  assert root.right.right.right.val == 4
  assert root.right.right.right.right.val == 5
  assert root.right.right.right.right.right.val == 6