from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        out = []
        freq=[]*(max(nums)+1)
        for num in nums:
            if freq[num]>=len(nums):
                out.append([])
            out[freq[num]].append(num)
            freq[num]+=1
        return out

nums=[1,3,4,1,2,3,1]
print(Solution().findMatrix(nums))