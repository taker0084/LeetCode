import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chrCount = collections.Counter(s)
        return len(set(chrCount.values())) == 1

s = "abacbc"
print(Solution().areOccurrencesEqual(s))