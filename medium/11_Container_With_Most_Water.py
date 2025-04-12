from turtle import forward
from typing import List

import pytest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        maxArea function returns the maximum amount of water a container can store

        Args:
            height (List[int]): a list of heights

        Returns:
            int: max amount of water
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if max_area < area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
#-------------TEST CASES-------------------------
@pytest.fixture
def solution():
    return Solution()

def test_maxArea(solution):
    """
    Example1: normal input
    """
    #Example1
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49