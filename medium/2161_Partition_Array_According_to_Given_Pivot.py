from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre = []
        post = []
        pivotCount = 0
        for num in nums:
            if num < pivot:
                pre.append(num)
            elif num > pivot:
                post.append(num)
            else: 
                pivotCount += 1
        return pre + [pivot] * pivotCount + post

nums = [-3,4,3,2]
pivot = 2
print(Solution().pivotArray(nums,pivot))