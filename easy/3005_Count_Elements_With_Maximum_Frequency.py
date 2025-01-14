import collections
from gc import collect
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numCount = collections.Counter(nums)
        maxCount = max(numCount.values())
        return sum(v==maxCount for v in numCount.values()) * maxCount

nums = [1,2,2,3,1,4]
print(Solution().maxFrequencyElements(nums))