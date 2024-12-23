from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    count-=1
                    break
        return count

allowed="abc"
words=["a","b","c","ab","ac","bc","abc"]
print(Solution().countConsistentStrings(allowed,words))