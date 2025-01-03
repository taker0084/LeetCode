import collections
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counter=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    counter+=1
        return counter

nums=[-1,1,2,3,1]
target = 2
print(Solution().countPairs(nums,target))