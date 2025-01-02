from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                out.append(nums[i+1])
        return out

nums = [1,2,3,4]
print(Solution().decompressRLElist(nums))