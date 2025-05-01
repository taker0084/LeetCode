import collections
import pytest
from returns.result import Failure, Success
from returns.pipeline import is_successful

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        This function determines if t can be constructed by converting characters from s

        Args:
            s (str): given string
            t (str): target string

        Returns:
            bool: whether t can construct by s or not
        """
        if not s or not t:
          return Failure("Input string cannot be empty")
        char_dict = collections.defaultdict(str)
        length_s = len(s)
        for i in range(length_s):
          if s[i] not in char_dict:
            if t[i] in char_dict.values():
              return Success(False)
            char_dict[s[i]] = t[i]
          if char_dict[s[i]] != t[i]:
            return Success(False)
        return Success(True)
#---------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()

def test_isIsomorphic(solution):
    """
    Example 1: normal true input
    Example 2: normal false input
    Example 3: input is empty
    """
    #Example1
    s = "egg"
    t = "add"
    expected = True
    result = Solution().isIsomorphic(s, t)
    assert is_successful(result)
    assert result.unwrap() == expected

    #Example2
    s = "foo"
    t = "bar"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert is_successful(result)
    assert result.unwrap() == expected
    
    #example3
    s = ""
    t = "baba"
    expected = False
    result = Solution().isIsomorphic(s, t)
    assert not is_successful(result)
    assert "Input string cannot be empty" in result.failure()
