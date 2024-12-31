from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        count = 0
        rowMaxes = []
        colMaxes = []
        size = len(grid)
        for i in range(size):
            rowMaxes.append(max(grid[i]))
            colMaxes.append(max(list(row[i] for row in grid)))
        for i in range(size):
            rowMax = rowMaxes[i]
            for j in range(size):
                count += min(rowMax,colMaxes[j]) - grid[j][i]
        return count

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))