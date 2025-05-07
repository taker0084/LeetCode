from typing import List
from returns.result import Success, Failure
import pytest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        The merge function takes a list of intervals and merges any overlapping intervals
        into a single interval. This is useful for simplifying a set of intervals by
        consolidating those that overlap.

        Args:
            intervals (List[List[int]]): Returns a list of merged intervals.
            If the input is invalid (empty), it returns a failure message.


        Returns:
            List[List[int]]: Returns a list of merged intervals.
            If the input is invalid (empty), it returns a failure message.
        """
        if not intervals:
            return Failure("Input mustn't be empty")
        merged_intervals = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        current_start = sorted_intervals[0][0]
        current_end = sorted_intervals[0][1]
        for start, end in sorted_intervals:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                merged_intervals.append([current_start, current_end])
                current_start = start
                current_end = end
        merged_intervals.append([current_start, current_end])
        return Success(merged_intervals)
#------------------TEST CASES---------------------------------------
@pytest.fixture
def solution():
    return Solution()
def test_merge(solution):
    """
    Example 1: Normal Input
    Example 2: Empty Input
    """
    #Example 1
    assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == Success([[1,6],[8,10],[15,18]])
    #Example 2
    assert solution.merge([]) == Failure("Input mustn't be empty")