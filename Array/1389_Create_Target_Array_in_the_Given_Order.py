from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            out.insert(index[i], nums[i])
        return out

nums= [0,1,2,3,4]
index = [0,1,2,2,1]
print(Solution().createTargetArray(nums,index))