from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = {}
        for i in range(len(names)):
            heightDict[heights[i]]=names[i]
        heights = sorted(heights, reverse=True)
        out = []
        for height in heights:
            out.append(heightDict[height])
        return out

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(Solution().sortPeople(names,heights))