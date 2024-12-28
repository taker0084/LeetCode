from math import e
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        max_candy=max(candies)
        for candy in candies:
            out.append(candy+extraCandies >= max_candy)
        return out

candies=[2,3,5,1,3]
extraCandies=3
print(Solution().kidsWithCandies(candies,extraCandies))