from typing import List
import pytest
from returns.result import Failure, Success


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        The insert method is designed to insert a new interval into a list of non-overlapping
        intervals and merge any overlapping intervals that may result from the insertion.

        Args:
            intervals (List[List[int]]): A list of existing intervals, where each interval is
            represented as a list of two integers (start and end).
            newInterval (List[int]): The new interval to be inserted, represented as a list
            of two integers.

        Returns:
            List[List[int]]: _description_
        """
        if not intervals or not newInterval:
            return Failure("Input mustn't be empty")
        intervals.append(newInterval)
        return Solution.merge_intervals(intervals)

    def merge_intervals(intervals: List[List[int]]):
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
def test_insert(solution):
    """
    Example 1: Normal Input
    Example 2: Empty Input
    """
    #Example 1
    assert solution.insert([[1,3],[6,9]], [2,5]) == Success([[1,5],[6,9]])
    #Example 2
    assert solution.insert([], [5,7]) == Failure("Input mustn't be empty")