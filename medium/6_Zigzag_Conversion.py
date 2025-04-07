from dataclasses import dataclass
from tabnanny import check

import pytest
@dataclass
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        convert converts zigzag route and read line by ine

        Args:
            s (str): input string
            numRows (int): a rows of zigzag lines

        Returns:
            str: output string
        """
        CHECK_NUM = (numRows-1) * 2
        rows_string = [''] * numRows
        if numRows == 1:
            return s
        for i in range(len(s)):
            if i % CHECK_NUM < numRows:
                rows_string[i % CHECK_NUM] += s[i]
            else:
                rows_string[CHECK_NUM - i % CHECK_NUM] += s[i]
        return ''.join(rows_string)
#-----------test case----------------
@pytest.fixture
def solution():
    return Solution()

def test_convert():
    """
    Test case to verify that the convert function returns the correct output

    Example1: normal input
    Example2: numRows = 1
    """
    #Example1
    s = "PAYPALISHIRING"
    numRows = 3
    assert Solution().convert(s, numRows) == "PAHNAPLSIIGYIR"
    #Example2
    s = "PAYPALISHIRING"
    numRows = 1
    assert Solution().convert(s, numRows) == "PAYPALISHIRING"