from tabnanny import check
import pytest
from returns.result import Failure, Success

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        The isHappy function determines whether a given integer n is a "happy number."
        A happy number is defined as a number that eventually reaches 1 when replaced by
        the sum of the square of its digits repeatedly. If it does not reach 1,
        it will enter a cycle that does not include 1, and thus it is not a happy number.

        Args:
            n (int): The integer to be checked for happiness.

        Returns:
            bool: Returns True if the number is a happy number, and False otherwise.
            If the input is invalid (e.g., negative or zero), it returns a failure message.
        """
        if not n:
            return Failure("Input mustn't be empty")
        if n < 0:
            return Failure("Input must be positive")
        check_value = n
        checked_list = set()
        while True:
            sum_square_digit = self.calculate_sum(check_value)
            if sum_square_digit == 1:
                return Success(True)
            if sum_square_digit in checked_list:
                return Success(False)
            checked_list.add(sum_square_digit)
            check_value = sum_square_digit

    def calculate_sum(self, check_value: int):
        """
        The calculate_sum function computes the sum of the squares of the digits of a given integer.
        This function is typically used in the context of determining whether a number is a happy number.

        Args:
            check_value (_type_): An integer whose digits will be squared and summed.

        Returns:
            _type_: The sum of the squares of the digits of check_value.
        """
        if not check_value:
            return Failure("Input mustn't be empty")
        if check_value < 0:
            return Failure("Input must be positive")
        sum_square_digit = 0
        while check_value:
            sum_square_digit += (check_value % 10) ** 2
            check_value = check_value // 10
        return sum_square_digit
#------------------TEST CASES---------------------------------------
@pytest.fixture
def solution():
    return Solution()
def test_isHappy(solution):
    """
    Example 1: Normal True Input
    Example 2: Normal False Input
    Example 3: Empty input
    Example 4: Negative input
    """
    #Example 1
    assert solution.isHappy(19) == Success(True)
    #Example 2
    assert solution.isHappy(2) == Success(False)
    #Example 3
    assert solution.isHappy("") == Failure("Input mustn't be empty")
    #Example 4
    assert solution.isHappy(-1) == Failure("Input must be positive")
def test_calculate_sum(solution):
    """
    Example 1: Normal Input
    Example 2: Empty Input
    Example 3: Negative Input
    """
    #Example 1
    assert solution.calculate_sum(19) == 82
    #Example 2
    assert solution.calculate_sum("") == Failure("Input mustn't be empty")
    #Example 3
    assert solution.calculate_sum(-1) == Failure("Input must be positive")