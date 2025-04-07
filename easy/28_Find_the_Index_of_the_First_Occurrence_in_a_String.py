import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        strStr returns index of the start position where needle begins within haystack else return -1

        Args:
            haystack (str): target string
            needle (str): contained string

        Returns:
            int: if start position else -1
        """
        if needle not in haystack:
            return -1
        length_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length_needle] == needle:
                return i
#--------------TEST CASES---------------------------
@pytest.fixture
def solution():
    return Solution()
def test_strStr_found(solution):
    """
    Test case to verify that the strStr function returns the correct index

    Example1: normal input
    Example2: not contained
    """
    #Example1
    haystack = "sadbutsad"
    needle = "sad"
    assert solution.strStr(haystack, needle) == 0
    #Example2
    haystack = "leetcode"
    needle = "leeto"
    assert solution.strStr(haystack, needle) == -1