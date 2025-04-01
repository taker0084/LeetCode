from typing import List
import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        this function returns a common prefix of strings in strs

        Args:
            strs (List[str]): a list of strings

        Returns:
            str: a common prefix
        """
        prefix = strs[0]
        for i in range(len(strs)):
            prefix = self.get_prefix(prefix, strs[i])
            if prefix == "":
                return ""
        return prefix
    
    def get_prefix(self, str1: str, str2: str) -> str:
        """
        this function returns a common prefix of two strings

        Args:
            str1 (str): a string
            str2 (str): other sting

        Returns:
            str: common prefix
        """
        prefix = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
        return prefix
#-------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_longestCommonPrefix(solution):
    """
    Example1: normal input with prefix
    Example2: normal input with no prefix
    """
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""