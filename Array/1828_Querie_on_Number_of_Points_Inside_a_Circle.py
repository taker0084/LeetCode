from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        out=[]
        for x,y,r in queries:
            count=0
            for px,py in points:
                if (x-px)**2+(y-py)**2<=r**2:
                    count+=1
            out.append(count)
        return out

points= [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(Solution().countPoints(points,queries))