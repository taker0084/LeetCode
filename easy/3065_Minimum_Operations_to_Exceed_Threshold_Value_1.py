from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0;
        for num in nums:
            if num < k:
                count += 1
        return count

nums= [2,11,10,1,3]
k = 10
print(Solution().minOperations(nums,k))