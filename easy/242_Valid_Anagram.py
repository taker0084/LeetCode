import pytest
from returns.result import Failure, Success
from returns.pipeline import is_successful
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        this function judges t is a anagram of s or not

        Args:
            s (str): a sentence
            t (str): a sentence which may be the anagram of s

        Returns:
            bool: whether t is an anagram of s or not
        """
        if not s or not t:
            return Failure("Input string cannot be empty")
        if len(s) != len(t):
            return Failure("The length of s and t must be the same")
        return Success(Counter(s) == Counter(t))
#---------------TEST CASES-------------------------
@pytest.fixture
def solution():
    return Solution()
def test_isAnagram(solution):
    """
    Example 1: normal true input
    Example 2: normal false input
    Example 3: input is empty
    Example 4: Input Length is not same
    """
    #Example1
    s = "anagram"
    t = "nagaram"
    expected = True
    result = solution.isAnagram(s, t)
    assert result.unwrap() == expected

    #Example2
    s = "rat"
    t = "car"
    expected = False
    result = solution.isAnagram(s, t)
    assert result.unwrap() == expected

    #Example3
    s = ""
    t = "car"
    expected = False
    result = solution.isAnagram(s, t)
    assert not is_successful(result)
    assert "Input string cannot be empty" in result.failure()

    #Example4
    s = "ab"
    t = "abab"
    expected = False
    result = solution.isAnagram(s, t)
    assert not is_successful(result)
    assert "The length of s and t must be the same" in result.failure()