from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for sentence in sentences:
            words = sentence.split()
            count = max(count, len(words))
        return count

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(Solution().mostWordsFound(sentences))