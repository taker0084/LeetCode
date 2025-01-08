from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.col = len(grid)
        self.row = len(grid[0])
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.pos[self.grid[i][j]]=(i,j)

    def adjacentSum(self, value: int) -> int:
        i,j = self.pos[value]
        n = self.grid[i-1][j] if i-1>=0 else 0
        s = self.grid[i+1][j] if i+1<len(self.grid) else 0
        w = self.grid[i][j-1] if j-1>=0 else 0
        e = self.grid[i][j+1] if j+1<len(self.grid[0]) else 0
        return n+s+w+e

    def diagonalSum(self, value: int) -> int:
        i,j = self.pos[value]
        nw = self.grid[i-1][j-1] if i-1>=0 and j-1>=0 else 0
        se = self.grid[i+1][j+1] if i+1<len(self.grid) and j+1<len(self.grid[0]) else 0
        sw = self.grid[i+1][j-1] if j-1>=0 and i+1<len(self.grid) else 0
        ne = self.grid[i-1][j+1] if j+1<len(self.grid[0]) and i-1>=0 else 0
        return nw+se+sw+ne


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)