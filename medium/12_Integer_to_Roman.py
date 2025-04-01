import pytest
class Solution:
    def intToRoman(self, num: int) -> str:
        """

        Args:
            num (int): an integer

        Returns:
            str: a letter converted from num
        """
        roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""
        for i in [1000, 100, 10, 1]:
            if num // i == 0:
                continue
            elif num // i == 4:
                ans += roman_dict[i] + roman_dict[i * 5]
            elif num // i == 9:
                ans += roman_dict[i] + roman_dict[i * 10]
            elif num // i < 4:
                ans += roman_dict[i] * (num // i)
            else:
                ans += roman_dict[i * 5] + roman_dict[i] * (num // i - 5)
            num = num % i
        return ans
#--------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_intToRoman(solution):
    """
    Example1: normal input
    """
    assert solution.intToRoman(1994) == "MCMXCIV"