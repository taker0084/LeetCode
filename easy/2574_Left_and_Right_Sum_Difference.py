from turtle import right
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        out=[]
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right-=nums[i]
            out.append(abs(left-right))
            left+=nums[i]
        return out

nums = [10,4,8,3]
print(Solution().leftRightDifference(nums))