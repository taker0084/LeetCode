from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        point_x=[point[0] for point in points]
        max=0
        point_x.sort()
        for i in range(len(point_x)-1):
            if max < point_x[i+1]-point_x[i]:
                max=point_x[i+1]-point_x[i]
        return max

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(Solution().maxWidthOfVerticalArea(points))