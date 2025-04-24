from typing import List, Tuple
import pytest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_place_list =  []
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] == 0:
                    zero_place_list.append((row_index, col_index))  # インデックスを追加
        for row, col in zero_place_list:
            for i in range(len(matrix)):
                matrix[i][col] = 0
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
#----------------TEST CASES----------------
@pytest.fixture
def solution():
  return Solution()

def test_setZeroes(solution):
    """
    Example 1, 2: normal input
    """
    #Example1
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[1,0,1],[0,0,0],[1,0,1]]
    solution.setZeroes(matrix)
    assert matrix == expected

    #Example2
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    solution.setZeroes(matrix)
    assert matrix == expected