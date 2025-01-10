from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        once = set()
        count = 0
        for word in words:
            if word[::-1] in once:
                count += 1
            else:
                once.add(word)
        return count

words = ["cd","ac","dc","ca","zz"]
print(Solution().maximumNumberOfStringPairs(words))