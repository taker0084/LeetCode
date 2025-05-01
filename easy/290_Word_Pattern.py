import collections
import pytest
from returns.result import Failure, Success
from returns.pipeline import is_successful

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        This function determines if s can be constructed by converting chars from pattern

        Args:
            pattern (str): input char
            s (str): target sentence

        Returns:
            bool: whether s can be constructed form pattern
        """
        if not pattern or not s:
            return Failure("Input string cannot be empty")
        words_list = s.split()
        if len(pattern) != len(words_list):
            return Failure("The length of pattern and words_list must be the same")
        char_word_dict = collections.defaultdict(str)
        char_length = len(pattern)
        for i in range(char_length):
            char = pattern[i]
            word = words_list[i]
            if char not in char_word_dict: 
                if word in char_word_dict.values():
                    return Success(False)
                char_word_dict[char] = word
            if char_word_dict[char] != word:
                return Success(False)
        return Success(True)
#---------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()
def test_wordPattern(solution):
    """
    Example 1: normal true input
    Example 2: normal false input
    Example 3: input is empty
    Example 4: Input Length is not same
    """
    #Example1
    pattern = "abba"
    s = "dog cat cat dog"
    expected = True
    result = Solution().wordPattern(pattern, s)
    assert result.unwrap() == expected

    #Example2
    pattern = "abba"
    s = "dog cat cat fish"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert result.unwrap() == expected

    #Example3
    pattern = ""
    s = "dog cat cat dog"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert not is_successful(result)
    assert "Input string cannot be empty" in result.failure()
    
    #Example4
    pattern = "abc"
    s = "dog cat cat dog"
    expected = False
    result = Solution().wordPattern(pattern, s)
    assert not is_successful(result)
    assert "The length of pattern and words_list must be the same" in result.failure()