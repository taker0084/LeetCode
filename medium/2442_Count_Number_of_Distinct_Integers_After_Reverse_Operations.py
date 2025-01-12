from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums+=[int(str(num)[::-1]) for num in nums]
        return len(set(nums))

nums=[1,13,10,12,31]
print(Solution().countDistinctIntegers(nums))