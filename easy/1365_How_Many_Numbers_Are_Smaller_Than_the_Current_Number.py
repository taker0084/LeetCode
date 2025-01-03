from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        out=[]
        for num in nums:
            count[num] += 1
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        for num in nums:
            out.append(count[num - 1] if num > 0 else 0)
        return out
        

nums=[8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))