import collections
from typing import List
from returns.result import Success, Failure
from returns.pipeline import is_successful


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The twoSum function takes a list of integers and a target integer,
        and it finds two distinct indices in the list such that
        the numbers at those indices add up to the target value.

        Args:
            nums (List[int]): A list of integers in which to search for two numbers
            that sum to the target.

            target (int): The target sum that the two numbers should equal.

        Returns:
            List[int]:
            A list containing the indices of the two numbers that add up to the target.
            If the input list is empty, it returns a failure message.
            If the list contains only one number, it returns 0.
        """
        if not nums:
          return Failure("Input list cannot be empty")
        if len(nums) == 1:
          return Failure("Input list must contain at least two numbers")
        source_num_dict = collections.defaultdict(int)
        for index, num in enumerate(nums):
          if (target - num) in source_num_dict:
            return Success([source_num_dict[target - num], index])
          source_num_dict[num] = index
#----------------TEST CASES----------------
import pytest
@pytest.fixture
def solution():
    return Solution()
def test_twoSum(solution):
    """
    Example 1: normal input
    Example 2: input is empty
    Example 3: input is too short
    """
    #Example1
    nums = [2,7,11,15]
    target = 9
    expected = Success([0,1])
    assert solution.twoSum(nums, target) == expected

    #Example2
    nums = []
    target = 6
    expected = False
    result = solution.twoSum(nums, target)
    assert not is_successful(result)
    assert "Input list cannot be empty" in result.failure()

    #Example3
    nums = [3]
    target = 6
    expected = Success([0,1])
    result = solution.twoSum(nums, target)
    assert not is_successful(result)
    assert "Input list must contain at least two numbers" in result.failure()