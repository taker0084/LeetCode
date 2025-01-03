from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        out=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                out[i][j] = max(max(row[j:j+3]) for row in grid[i:i+3])  # 修正箇所
        return out

grid=[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(Solution().largestLocal(grid))