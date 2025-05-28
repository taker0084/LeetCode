import collections
from typing import List
from returns.result import Success, Failure
import pytest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate a reverse Polish notation expression.
        Args:
            tokens (List[str]): A list of strings representing the tokens in the expression.
        Returns:
            int: The result of the expression.
        """
        if not tokens:
            return Failure(0)
        stack = collections.deque()
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                match token:
                    case '+':
                        stack.append(self.add(num1, num2))
                    case '-':
                        stack.append(self.subtract(num1, num2))
                    case '*':
                        stack.append(self.multiply(num1, num2))
                    case '/':
                        stack.append(self.divide(num1, num2))
            else:
                stack.append(int(token))
        return Success(stack[0])

    def add(self, num1: int, num2: int) -> int:
        """
        Add two numbers.
        """
        return num1 + num2

    def subtract(self, num1: int, num2: int) -> int:
        """
        Subtract two numbers.
        """
        return num1 - num2

    def multiply(self, num1: int, num2: int) -> int:
        """
        Multiply two numbers.
        """
        return num1 * num2

    def divide(self, num1: int, num2: int) -> int:
        """
        Divide two numbers.
        """
        return int(num1 / num2)

#-------------------TEST CASES-------------------
@pytest.fixture
def solution():
    return Solution()

def test_evalRPN(solution):
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == Success(9)
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == Success(6)
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == Success(22)
    assert solution.evalRPN([]) == Failure(0)
