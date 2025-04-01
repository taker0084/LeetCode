import pytest
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        separated_word = s.split()
        return len(separated_word[-1])
#-------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_lengthOfLastWord(solution):
    """
    Example1: normal input
    """
    assert solution.lengthOfLastWord("Hello World") == 5