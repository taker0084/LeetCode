from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise=0
        for i in range(len(nums)-1):
            bitwise=nums[i]|nums[i+1]
            if bitwise>max_bitwise:
                max_bitwise=bitwise
        

nums=[3,2,1,5]
print(Solution().countMaxOrSubsets(nums))
    