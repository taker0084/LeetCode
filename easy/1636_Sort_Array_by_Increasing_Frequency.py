import collections
from gc import collect
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCount = collections.Counter(nums)
        numCount = sorted(numCount.items(), key=lambda item: (item[1],-item[0])) ##item[1](出現回数)でソート, 同じ場合はitem[0](値)の大きい順
        ans = []
        for num in numCount:
            ans.extend([num[0]]*num[1])
        return ans

nums=[-1,1,-6,4,5,-6,1,4,1]
print(Solution().frequencySort(nums))