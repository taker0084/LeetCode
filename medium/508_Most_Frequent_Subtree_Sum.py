from typing import List, Optional
import collections
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        findFrequentTreeSum returns sum of subtree which occurring the most

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            List[int]: _description_
        """
        if not root:
          return []
        sum_count_dict = collections.defaultdict(int)
        def dfs(node):
          if not node:
            return 0
          left_sum = dfs(node.left)
          right_sum = dfs(node.right)
          total_sum = left_sum + right_sum + node.val
          sum_count_dict[total_sum] += 1
          return total_sum
        _ = dfs(root)

        max_count = max(sum_count_dict.values())
        return [key for key, value in sum_count_dict.items() if value == max_count]
#------Test CASES------
@pytest.fixture
def solution():
  return Solution()

def test_findFrequentTreeSum(solution):
  #example1
  root = TreeNode(5, TreeNode(2), TreeNode(-3))
  assert solution.findFrequentTreeSum(root) == [2, -3, 4]
  #example2
  root = TreeNode(5, TreeNode(2), TreeNode(-5))
  assert solution.findFrequentTreeSum(root) == [2]