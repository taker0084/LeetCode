from typing import List
import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        setNum = collections.Counter(nums)
        onceNum = []
        for k, v in setNum.items():
            if v == 1:
                onceNum.append(k)
        return sum(onceNum)

nums = [1,2,3,2]
print(Solution().sumOfUnique(nums))