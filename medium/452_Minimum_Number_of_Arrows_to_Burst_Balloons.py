from typing import List
import pytest
from returns.result import Failure, Success

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        The findMinArrowShots function determines the minimum number of arrows
        needed to burst all balloons represented by a list of intervals.
        Each interval represents the start and end points of a balloon,
        and an arrow can burst a balloon if it hits any point within that interval.

        Args:
            points (List[List[int]]): A list of intervals, where each interval is
            represented as a list of two integers (start and end).

        Returns:
            int: The minimum number of arrows required to burst all balloons.
            If the input is invalid (empty), it returns a failure message.
        """
        if not points:
            return Failure("No balloons to burst")
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points:
            if start > current_end:
                arrows += 1
                current_end = end
        return Success(arrows)
#----------------TEST CASES-------------------
@pytest.fixture
def solution():
    return Solution()
def test_solution(solution):
    """
    # Test case 1: Normal case with overlapping intervals
    # Test case 2: No balloons
    """
    # Test case 1: Normal case with overlapping intervals
    points = [[10,16],[2,8],[1,6],[7,12]]
    assert solution.findMinArrowShots(points) == Success(2)

    # Test case 2: No balloons
    points = []
    assert solution.findMinArrowShots(points) == Failure("No balloons to burst")