from typing import List
from returns.result import Failure, Success
import pytest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The longestConsecutive function determines the length of the longest consecutive
        sequence of integers in a given list. A consecutive sequence is defined as a sequence
        of numbers where each number is exactly one greater than the previous number.


        Args:
            nums (List[int]): A list of integers from which to find the longest consecutive sequence.

        Returns:
            int: Returns the length of the longest consecutive sequence found in the list.
            If the input is invalid (empty), it returns a failure message.
        """
        if not nums:
            return Failure("Input mustn't be empty")
        longest_consecutive = 1
        
        sorted_sets = sorted(set(nums))
        length = 1
        for i in range(1, len(sorted_sets)):
            if sorted_sets[i] - sorted_sets[i-1] == 1:
                length += 1
            else:
                length = 1
            if length > longest_consecutive:
                longest_consecutive = length
        return Success(longest_consecutive)
#--------------TEST CASES---------------------------------------
@pytest.fixture
def solution():
    return Solution()
def test_longestConsecutive(solution):
    """
    Example 1: Normal Input
    Example 2: Empty Input
    """
    #Example 1
    assert solution.longestConsecutive([100,4,200,1,3,2]) == Success(4)
    #Example 2
    assert solution.longestConsecutive([]) == Failure("Input mustn't be empty")