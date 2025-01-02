from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        out = 0;
        for i in range(len(nums)):
            if i.bit_count() == k:
                out += nums[i]
        return out

nums= [5,10,1,5,2]
k = 1
print(Solution().sumIndicesWithKSetBits(nums,k))