import collections
from typing import List
from returns.result import Success, Failure
import pytest


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        The containsNearbyDuplicate function checks if there are two distinct indices
        in a list of integers such that the values at those indices are equal and
        the absolute difference between the indices is at most k.

        Args:
            nums (List[int]):  A list of integers to be checked for nearby duplicates.
            k (int): The maximum allowed index difference between the duplicate elements.

        Returns:
            bool: Returns True if there are two indices i and j such that nums[i] == nums[j] 
            and |i-j|≤k. Returns False otherwise. If the input is invalid, it returns a failure message.
        """
        if not nums:
            return Failure("Input mustn't be empty")
        if len(nums) == 1:
            return Failure("Input must have more than 1 element")
        if k <= 0:
            return Failure("k must be positive")
        if len(set(nums)) == len(nums):
            return Failure("Input must have duplicate elements")

        first_num_place = collections.defaultdict(int)

        for i, num in enumerate(nums):
            if num in first_num_place and i - first_num_place[num] <= k:
                return Success(True)
            first_num_place[num] = i
        return Success(False)
#--------------TEST CASES---------------------------------------
@pytest.fixture
def solution():
    return Solution()
def test_containsNearbyDuplicate(solution):
    """
    Example 1: Normal True Input
    Example 2: Normal False Input
    Example 3: Empty input
    Example 4: single input
    Example 5: k = 0
    Example 6: No duplicate elements
    """
    #Example 1
    assert solution.containsNearbyDuplicate([1,2,3,1], 3) == Success(True)
    #Example 2
    assert solution.containsNearbyDuplicate([1,2,3,1,2,3], 2) == Success(False)
    #Example 3
    assert solution.containsNearbyDuplicate([], 0) == Failure("Input mustn't be empty")
    #Example 4
    assert solution.containsNearbyDuplicate([1], 3) == Failure("Input must have more than 1 element")
    #Example 5
    assert solution.containsNearbyDuplicate([1,2,3,1], 0) == Failure("k must be positive")
    #Example 6
    assert solution.containsNearbyDuplicate([1,2,3,4], 3) == Failure("Input must have duplicate elements")