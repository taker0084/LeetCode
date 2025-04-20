from typing import List

import pytest


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        this functions judges whether input List satisfies the Sudoku conditions

        Args:
            board (List[List[str]]): input list

        Returns:
            bool: whether input satisfies Sudoku conditions or not
        """
        is_valid_row = self.validRow(board)
        if not is_valid_row:
            return False
        is_valid_column = self.validColumn(board)
        if not is_valid_column:
            return False
        is_valid_box = self.validBox(board)
        if not is_valid_box:
            return False
        return True

    def validUnit(self, unit: List[str]) -> bool:
        """
        this function judges whether the unit area of input List satisfies the conditions

        Args:
            unit (List[str]): a part of inputs

        Returns:
            bool: satisfies conditions or not
        """
        unit = [i for i in unit if i != "."]
        return len(unit) == len(set(unit))

    def validRow(self, board: List[List[str]]) -> bool:
        """
        this function judges whether the row area of input List satisfies the conditions

        Args:
            board (List[List[str]]): input

        Returns:
            bool: satisfies conditions or not
        """
        for row in board:
            if not self.validUnit(row):
                return False
        return True

    def validColumn(self, board: List[List[str]]) -> bool:
        """
        this function judges whether the column area of input List satisfies the conditions

        Args:
            board (List[List[str]]): inputs

        Returns:
            bool: satisfies conditions or not
        """
        for col in zip(*board):
            if not self.validUnit(col):
                return False
        return True

    def validBox(self, board: List[List[str]]) -> bool:
        """
        this function judges whether the box area of input List satisfies the conditions

        Args:
            board (List[List[str]]): inputs

        Returns:
            bool: satisfies conditions or not
        """
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.validUnit(square):
                    return False
        return True
#-------------------TEST CASES-------------------------
@pytest.fixture
def solution():
    return Solution()
def test_is_valid_sudoku(solution):
    """
    Example1: True Input
    Example2: False Input
    """
    #Example1
    #True Input
    assert solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
                                ,["6",".",".","1","9","5",".",".","."]
                                ,[".","9","8",".",".",".",".","6","."]
                                ,["8",".",".",".","6",".",".",".","3"]
                                ,["4",".",".","8",".","3",".",".","1"]
                                ,["7",".",".",".","2",".",".",".","6"]
                                ,[".","6",".",".",".",".","2","8","."]
                                ,[".",".",".","4","1","9",".",".","5"]
                                ,[".",".",".",".","8",".",".","7","9"]]) == True
    #Example2
    #False Input
    assert solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                                ,["6",".",".","1","9","5",".",".","."]
                                ,[".","9","8",".",".",".",".","6","."]
                                ,["8",".",".",".","6",".",".",".","3"]
                                ,["4",".",".","8",".","3",".",".","1"]
                                ,["7",".",".",".","2",".",".",".","6"]
                                ,[".","6",".",".",".",".","2","8","."]
                                ,[".",".",".","4","1","9",".",".","5"]
                                ,[".",".",".",".","8",".",".","7","9"]]) == False

def test_valid_unit(solution):
    """
    Example1: True Input
    Example2: False Input
    """
    #Example1
    #True Input
    assert solution.validUnit(["5","3",".",".","7",".",".",".","."]) == True
    #Example2
    #False Input
    assert solution.validUnit(["8","3",".",".","8",".",".",".","."]) == False