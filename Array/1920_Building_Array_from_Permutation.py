from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
          ans.append(nums[nums[i]])
        return ans

nums=[0,2,1,5,3,4]
print(Solution().buildArray(nums))