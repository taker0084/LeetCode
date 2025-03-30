import collections
from typing import List

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        distanceK returns a list of nodes which has k distance from target

        Args:
            root (TreeNode): a root node of tree
            target (TreeNode): target node
            k (int): target distance

        Returns:
            List[int]: _description_
        """
        ans = []
        neighbor = collections.defaultdict(list)
        current_level_nodes = collections.deque([(root, None)])
        while current_level_nodes:
          node,parent = current_level_nodes.popleft()
          if node.left:
              current_level_nodes.append((node.left, node))
              neighbor[node].append(node.left)
          if node.right:
            current_level_nodes.append((node.right, node))
            neighbor[node].append(node.right)
          neighbor[node].append(parent)

        visited = set()
        current_distance_nodes = collections.deque([(target, 0)])
        while current_distance_nodes:
          node, distance = current_distance_nodes.popleft()
          if distance == k:
            ans.append(node.val)
          if node not in visited:
            visited.add(node)
            for neighbor_node in neighbor[node]:
              if neighbor_node and neighbor_node not in visited:
                current_distance_nodes.append((neighbor_node, distance + 1))
        return ans
#-----------TEST CASES----------------
@pytest.fixture
def solution():
  return Solution()

def test_distanceK(solution):
    """
    Example1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    """
    #Example1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    target = TreeNode(5)
    k = 2
    expected = [7,4,1]
    assert solution.distanceK(root, target, k) == expected