import collections
from typing import Counter, List
import pytest


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        minSubArrayLen returns the minimum length of a contiguous subarray of which the sum is greater than or equal to target

        Args:
            target (int): target sum value 
            nums (List[int]): a list of integers

        Returns:
            int: a minimum length
        """
        if target > sum(nums):
            return 0
        left, right = 0, 0
        min_length = float('inf')
        for right in range(len(nums)):
            sum_sub_array = sum(nums[left:right+1])
            while sum_sub_array >= target:
                min_length = min(min_length, right - left + 1)
                sum_sub_array -= nums[left]
                left += 1
        return min_length
#-----------------TESTCASES-------------------------
@pytest.fixture
def solution():
    return Solution()

def test_minSubArrayLen(solution):
    """
    Example1: normal input
    Example2: exists target value itself
    Example3: input list doesn't have valid subArray
    """
    #Example1
    assert solution.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    #Example2
    assert solution.minSubArrayLen(4, [1,4,4]) == 1
    #Example3
    assert solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0