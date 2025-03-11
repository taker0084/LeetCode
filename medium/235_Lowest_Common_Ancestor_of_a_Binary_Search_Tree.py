# Definition for a binary tree node.
import pytest
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        lowestCommonAncestor returns lowest common ancestor of two node p, q

        Args:
            root (TreeNode): root node
            p (TreeNode): specify node
            q (TreeNode): specify node

        Returns:
            TreeNode: lowest common node
        """
        if not root:
          return
        self.parent = None
        def dfs(node):
          if not node:
            return False
          left_contain_node = dfs(node.left)
          right_contain_node = dfs(node.right)
          return self.count_true(left_contain_node, right_contain_node, node, p, q)
        dfs(root)
        return self.parent

    def count_true(self, left: bool, right: bool, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        """
        count_true judges current_node is parent and this subtree contains node p, q

        Args:
            left (bool): Does left subtree has node p or q ?
            right (bool): Does left subtree has node p or q ?
            node (TreeNode): current node
            p (TreeNode):
            q (TreeNode):

        Returns:
            bool: _description_
        """
        count = 0
        if left:
          count += 1
        if right:
          count += 1
        if node.val == p.val or node.val == q.val:
          count += 1

        if count >= 2:
          self.parent = node
        return count == 1
#------Test CASES------
@pytest.fixture
def solution():
  return Solution()

def test_lowestCommonAncestor(solution):
  #example1
  root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
  p = TreeNode(5)
  q = TreeNode(1)
  assert solution.lowestCommonAncestor(root, p, q).val == 3
  #example2
  root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
  p = TreeNode(5)
  q = TreeNode(4)
  assert solution.lowestCommonAncestor(root, p, q).val == 5
  #example3
  root = TreeNode(1, TreeNode(2), TreeNode(3))
  p = TreeNode(2)
  q = TreeNode(3)
  assert solution.lowestCommonAncestor(root, p, q).val == 1