from tabnanny import check
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        next_board = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                live_neighbor = self.check_neighbors(board, row, col)
                if board[row][col] == 1 and live_neighbor not in [2, 3]:
                    next_board[row][col] = 0
                elif board[row][col] == 0 and live_neighbor == 3:
                    next_board[row][col] = 1
                else:
                    next_board[row][col] = board[row][col]
        for row in range(rows):
            for col in range(cols):
                board[row][col] = next_board[row][col]

    def check_neighbors(self, board: List[List[int]], target_row: int, target_col: int):
        live_neighbors = 0
        for row in range(max(0, target_row - 1), min(len(board), target_row + 2)):
            for col in range(max(0, target_col - 1), min(len(board[0]), target_col + 2)):
                if (row != target_row or col != target_col) and board[row][col] == 1:
                    live_neighbors += 1
        return live_neighbors
#----------------------TEST CASES----------------------
import pytest
@pytest.fixture
def solution():
  return Solution()

def test_gameofLife(solution):
    """
    Example 1: normal input
    """
    #Example1
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    solution.gameOfLife(board)
    assert board == expected

def test_check_neighbors(solution):
    """
    Example 1: normal input
    """
    #Example1
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    expected = 1
    assert solution.check_neighbors(board, 0, 0) == expected