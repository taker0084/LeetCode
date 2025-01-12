from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNum1 = set(nums1)
        setNum2 = set(nums2)
        ans1=[]
        ans2=[]
        for num in setNum1:
            if num not in setNum2:
                ans1.append(num)
        for num in setNum2:
            if num not in setNum1:
                ans2.append(num)
        return [ans1, ans2]

nums1=[1,2,3]
nums2=[2,4,6]
print(Solution().findDifference(nums1, nums2))