from dataclasses import dataclass
from tabnanny import check
@dataclass
class Solution:
    def convert(self, s: str, numRows: int) -> str:
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