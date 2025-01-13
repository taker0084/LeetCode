import collections
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        dict=collections.defaultdict(list)
        length = len(A)
        count = 0
        for i in range(length):
            if A[i] not in dict:
                dict[A[i]] = [i]
            else:
                count += 1
            if B[i] not in dict:
                dict[B[i]] = [i]
            else:
                count += 1
            ans.append(count)
        return ans

A = [1,3,2,4]
B = [3,1,2,4]
print(Solution().findThePrefixCommonArray(A, B))