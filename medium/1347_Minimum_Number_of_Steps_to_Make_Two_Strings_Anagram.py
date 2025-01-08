import collections
from typing import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for char in set(s):
            countS = s.count(char)
            countT = t.count(char)
            if countS>countT:
                count += countS-countT
        return count

s = "anagram"
t = "mangaar"
print(Solution().minSteps(s,t))