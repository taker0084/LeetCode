from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # パターンを数えるカウンターを用意
        patterns = Counter()
        for row in matrix:
            #最初が1から始まる状態で登録、0始まりは全てbitを反転
            pattern = tuple(row)
            if row[0]:
                pattern = tuple([0 if i else 1 for i in row])
            patterns[pattern] += 1
        return max(patterns.values())

matrix = [[0,1],[1,1]]
print(Solution().maxEqualRowsAfterFlips(matrix))