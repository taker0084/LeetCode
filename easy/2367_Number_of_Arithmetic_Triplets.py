from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        out = 0
        for i in range(1, len(nums)-1):
            if nums[i]-diff in nums[:i] and nums[i]+diff in nums[i+1:]:
                out += 1
        return out

nums = [4,5,6,7,8,9]
diff = 2
print(Solution().arithmeticTriplets(nums,diff))