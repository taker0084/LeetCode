from itertools import count
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count=0
        for num1 in nums1:
            for num2 in nums2:
                if num1%(num2*k)==0:
                    count+=1
        return count

nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
print(Solution().numberOfPairs(nums1,nums2,k))