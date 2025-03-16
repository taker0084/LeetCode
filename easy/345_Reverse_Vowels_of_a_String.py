import pytest
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        reverseVowels:
          reverse only vowels in given string

        Args:
            s (str): given string

        Returns:
            str: reversed string
        """
        if len(s) == 1:
          return s
        vowels = "aeiouAEIOU"
        list_s = list(s)
        left_index, right_index = 0, len(s)-1
        while left_index < right_index:
          if list_s[left_index] not in vowels:
            left_index += 1
          elif list_s[right_index] not in vowels:
            right_index -= 1
          else:
            list_s[left_index], list_s[right_index] = list_s[right_index], list_s[left_index]
            left_index += 1
            right_index -= 1
        return "".join(list_s)
#--------TEST---------------------------
@pytest.fixture
def solution():
  return Solution()

def test_reverseVowels(solution):
    """
    Example1: normal case
    Example2: if string is only one character
    Example3: if string is empty
    """
    #Example1
    s = "hello"
    assert solution.reverseVowels(s) == "holle"
    #Example2
    s = "a"
    assert solution.reverseVowels(s) == "a"
    #Example3
    s = ""
    assert solution.reverseVowels(s) == ""