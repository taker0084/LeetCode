import collections
from typing import Optional

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        """
        self.root: a root of complete binary tree
        self.parent_queue: a list of node which doesn't have node.left or node.right

        Args:
            root (Optional[TreeNode]): a root of binary tree
        """
        self.root = root
        self.parent_queue = collections.deque()
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.parent_queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        """
        insert a node to complete binary tree

        Args:
            val (int): a value of input node

        Returns:
            int: a value of parent's node
        """
        parent = self.parent_queue[0]
        new_node = TreeNode(val)
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.parent_queue.popleft()
        self.parent_queue.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

#---------TEST CASES----------------
@pytest.fixture
def root():
    return TreeNode()
def test_CBTInserter():
    """
    Example1: normal tree case
    """
    #Example1
    root = TreeNode(1, TreeNode(2))
    obj = CBTInserter(root)
    assert obj.insert(3) == 1
    assert obj.insert(4) == 2
    assert obj.get_root() == root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()