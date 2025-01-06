import collections
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        diffDict = {};
        count = 0;
        for num in nums:
            diffDict[num] = diffDict.get(num, 0) + 1;
        for key in diffDict.keys():
            if key-k in diffDict:
                count += diffDict[key - k]
        return count

nums = [1,3,5,7,9];
k = 2;
print(Solution().countKDifference(nums,k));