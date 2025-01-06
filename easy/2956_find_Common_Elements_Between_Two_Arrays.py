from gc import collect
import collections
from itertools import count
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dict = collections.Counter(nums1)
        num2Dict = collections.Counter(nums2)
        count1 = 0
        count2 = 0
        for num1 in nums1:
            if num1 in num2Dict:
                count1 += 1
        for num2 in nums2:
            if num2 in num1Dict:
                count2 += 1
        return [count1, count2]

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(Solution().findIntersectionValues(nums1, nums2))