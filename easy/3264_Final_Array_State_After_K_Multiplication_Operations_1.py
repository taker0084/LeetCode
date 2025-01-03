from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # heapq.heapify(nums)
        # for k in range(k):
        #     heapq.heappush(nums, heapq.heappop(nums)*multiplier)
        # return nums
        for k in range(k):
            nums[nums.index(min(nums))]*=multiplier
        return nums
      
nums=[2,1,3,5,6]
k=5
multiplier=2
print(Solution().getFinalState(nums,k,multiplier))