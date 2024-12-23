from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i%3!=0:
                count+=1
        return count

nums=[1,2,3,4]
print(Solution().minimumOperations(nums))