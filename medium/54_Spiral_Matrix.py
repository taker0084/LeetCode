from typing import List

import pytest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        this function returns a list of index which is located as spiral order

        Args:
            matrix (List[List[int]]): spiral order

        Returns:
            List[int]: a one-dimension list
        """
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
#----------------TEST CASES----------------
@pytest.fixture
def solution():
  return Solution()

def test_spiralOrder(solution):
    """
    Example 1: normal input
    """
    #Example1
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    assert solution.spiralOrder(matrix) == expected