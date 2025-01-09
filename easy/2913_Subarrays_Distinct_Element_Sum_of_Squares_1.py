from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            unique = set()
            for j in range(i,len(nums)):
                unique.add(nums[j])
                count += len(unique)**2
        return count

nums = [1,2,1]
print(Solution().sumCounts(nums))