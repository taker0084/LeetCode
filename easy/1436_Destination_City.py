from os import path
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dictFrom =[]
        dictTo = []
        for path in paths:
            dictFrom.append(path[0])
            dictTo.append(path[1])
        return list(set(dictTo) - set(dictFrom))[0]

paths=[["B","C"],["D","B"],["C","A"]]
print(Solution().destCity(paths))