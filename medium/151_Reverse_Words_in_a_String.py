import re

import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        this function returns reversed sentence

        Args:
            s (str): sentence

        Returns:
            str: reversed sentence
        """
        words = s.split()
        reverse_words = words[::-1]
        return " ".join(reverse_words)
#-------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_reverseWords(solution):
    """
    Example1: normal input
    """
    assert solution.reverseWords("the sky is blue") == "blue is sky the"