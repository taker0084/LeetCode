import pytest
from returns.result import Success, Failure

class Solution:
    def isValid(self, s: str) -> bool:
        """
        The isValid function checks whether a given string of parentheses is valid.
        A string is considered valid if every opening bracket has a corresponding
        closing bracket in the correct order.

        Args:
            s (str): A string containing only the characters
            '(', ')', '{', '}', '[',and ']'.


        Returns:
            bool: Returns True if the string is valid, and False otherwise.
        """
        if not s or len(s) % 2 != 0:
            return Failure(False)
        start_parenthesis = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = start_parenthesis.pop() if start_parenthesis else ''
                if mapping[char] != top_element:
                    return Failure(False)
            else:
                start_parenthesis.append(char)
        return Success(not start_parenthesis)
#-------------------TEST CASES-------------------
@pytest.fixture
def solution():
    return Solution()

def test_solution(solution):
    assert solution.isValid("()") == Success(True)
    assert solution.isValid("(]") == Failure(False)