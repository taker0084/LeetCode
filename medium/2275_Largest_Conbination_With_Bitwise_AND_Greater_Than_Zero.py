import collections
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bitCount = [0] * 24  #各ビットが何回使われているか
        for i in range(24):
            for num in candidates:
                if num & (1 << i):
                    bitCount[i] += 1    #numが2進数でi桁目を含む場合、bitCountのi番目の要素に1を足す
        return

candidates = [16,17,71,62,12,24,14]
print(Solution().largestCombination(candidates))