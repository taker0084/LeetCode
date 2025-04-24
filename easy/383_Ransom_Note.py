import collections

import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        This function returns True if ransomNote can be constructed by using the letters from magazine and False otherwise.
        
        Args:
            ransomNote (str): target sentence
            magazine (str): a list of word which we can use to construct the target sentence

        Returns:
            bool: able to construct the sentence by using magazine
        """
        magazine_counter = collections.Counter(magazine)
        ransomNote_counter = collections.Counter(ransomNote)
        set_ransomNote = set(ransomNote)
        for char in set_ransomNote:
            if char not in magazine_counter:
                return False
            if ransomNote_counter[char] > magazine_counter[char]:
                return False
        return True
#---------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()
def test_canConstruct(solution):
    """
    Example 1: normal false input
    Example 2: normal true input
    """
    #Example1
    ransomNote = "a"
    magazine = "b"
    expected = False
    assert Solution().canConstruct(ransomNote, magazine) == expected

    #Example2
    ransomNote = "aa"
    magazine = "aab"
    expected = True
    assert Solution().canConstruct(ransomNote, magazine) == expected