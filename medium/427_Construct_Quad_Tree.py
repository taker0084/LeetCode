"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.dfs(grid, 0, 0, len(grid))

    def dfs(self, grid, x, y, size):
        if self.isLeaf(grid, x, y, size):
            return Node(grid[x][y], True)
        half = size // 2
        topLeft = self.dfs(grid, x, y, half)
        topRight = self.dfs(grid, x, y + half, half)
        bottomLeft = self.dfs(grid, x + half, y, half)
        bottomRight = self.dfs(grid, x + half, y + half, half)
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

    def isLeaf(self, grid, x, y, size):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != grid[x][y]:
                    return False
        return True