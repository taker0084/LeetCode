import string
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = string.ascii_lowercase
        morseWords = []
        for word in words:
            morseWord = ""
            for char in word:
                morseWord += morseList[alphabet.index(char)]
            morseWords.append(morseWord)
        setMorseWords = set(morseWords)
        return len(setMorseWords)

words = ["gin","zen","gig","msg"]
print(Solution().uniqueMorseRepresentations(words))