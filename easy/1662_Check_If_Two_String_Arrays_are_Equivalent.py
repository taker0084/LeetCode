from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = "".join(word1)
        word2 = "".join(word2)
        return word1==word2

word1 = ["abc", "d", "defg"]
word2= ["abcddefg"]
print(Solution().arrayStringsAreEqual(word1,word2))