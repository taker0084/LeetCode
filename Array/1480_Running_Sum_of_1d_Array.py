from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out=[]
        sum=0
        for num in nums:
            sum+=num
            out.append(sum)
        return out

nums=[1,2,3,4]
print(Solution().runningSum(nums))