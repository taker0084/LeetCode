from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(index, nums):
          if not nums:
            return
          middle = len(nums)//2
          print(middle)
          node = TreeNode(nums[middle])
          node.left = makeBST(middle, nums[:middle])
          node.right = makeBST(middle, nums[middle+1:])
          return node
        return makeBST(0,nums)