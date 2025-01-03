from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorValue = nums[0]
        for i in range(1, len(nums)):
            xorValue ^= nums[i]
        xorValue ^= k
        return xorValue.bit_count()

nums = [2,1,3,4]
k = 1
print(Solution().minOperations(nums,k))