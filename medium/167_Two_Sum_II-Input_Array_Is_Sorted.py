import collections
from operator import index
from typing import List
import pytest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        this function finds a pair of two integers that their sum is equal to target

        Args:
            numbers (List[int]): integer list
            target (int): target value

        Returns:
            List[int]: a pair of integers' index
        """
        nums_pair_dict = collections.defaultdict(int)
        for index, num in enumerate(numbers):
            if target - num in nums_pair_dict:
                return [nums_pair_dict[target - num]+1, index+1]
            nums_pair_dict[num]=index
#------------TEST CASE----------------
@pytest.fixture
def solution():
    return Solution()

def test_twoSum(solution):
    """
    Test case to verify that the twoSum function returns the correct output

    Example1: true case
    """
    # Example1
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]