import collections

import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        this function converts roman string to integer

        Args:
            s (str): a roman string

        Returns:
            int: an integer that converted from s
        """
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        return result + romans[s[-1]]
#--------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_romanToInt(solution):
    assert solution.romanToInt("MCMXCIV") == 1994