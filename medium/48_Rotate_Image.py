from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        this function returns rotate matrix
        """
        #matrix[::-1] is reverse of matrix
        matrix[:] = zip(*matrix[::-1])