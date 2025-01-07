import collections


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        if sentence.isalpha() == False:
            return False
        dict = collections.Counter(sentence)
        if len(dict) == 26:
            return True
        return False

sentence="thequickbrownfoxjumpsoverthelazydog"
print(Solution().checkIfPangram(sentence))