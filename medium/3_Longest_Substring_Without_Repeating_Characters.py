from tracemalloc import start
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        this function returns longest sub array string which doesn't appear same character twice

        Args:
            s (str): input string

        Returns:
            int: length of longest sub array string
        """
        exist_char = set()
        start = 0
        max_len = 0
        for i in range(len(s)):
            while s[i] in exist_char:
                exist_char.remove(s[start])
                start += 1
            exist_char.add(s[i])
            max_len = max(max_len, i - start + 1)
        return max_len

        # exist_char = {}
        # start = 0
        # max_len = 0
        # for i in range(len(s)):
        #     if s[i] in exist_char and start <= exist_char[s[i]]:
        #         max_len = max(max_len, i - start)
        #         start = exist_char[s[i]] + 1
        #         exist_char[s[i]] = i
        #     exist_char[s[i]] = i
        # return max(max_len, len(s) - start)


# -------------TEST CASES-------------------------
@pytest.fixture
def solution():
    return Solution()


def test_lengthOfLongestSubstring(solution):
    """
    Example1: normal input
    Example2: input string is empty
    Example3: input string is only one character
    Example4: input string is all same character
    """
    # Example1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    # Example2
    assert solution.lengthOfLongestSubstring("") == 0
    # Example3
    assert solution.lengthOfLongestSubstring("a") == 1
    # Example4
    assert solution.lengthOfLongestSubstring("aaaaa") == 1
