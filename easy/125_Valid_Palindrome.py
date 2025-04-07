import re
import pytest
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        isPalindrome returns the sentence is equal to reversed sentence or not

        Args:
            s (str): input

        Returns:
            bool: equal or not
        """
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        words = s.split()
        s = "".join(words).lower()
        return s[::-1] == s
#--------------TEST CASES---------------------------
@pytest.fixture
def solution():
    return Solution()

def test_isPalindrome(solution):
    """
    Test case to verify that the isPalindrome function returns true answer

    Example1: true case
    Example2: false case
    """
    # Example1
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    # Example2
    assert solution.isPalindrome("race a car") == False