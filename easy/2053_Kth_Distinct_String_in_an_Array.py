from os import remove
from typing import Counter, List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict = {}
        for char in arr:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        once = [key for key,value in dict.items() if value==1]
        if len(once) < k:
            return ""
        return once[k-1]
arr = ["d","b","c","b","c","a"]
k = 2
print(Solution().kthDistinct(arr,k))
