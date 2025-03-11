import collections
from operator import ne
from typing import List

import pytest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        summaryRanges() returns small sorted list from List
        Args:
            nums (List[int]): list of value

        Returns:
            List[str]: small sorted list using "->"(string)
        """

        ans = []
        if not nums:
          return ans
        next_expected_num = nums[0]
        small_sorted_list = []
        nums_size = len(nums)

        for index in range(nums_size):
          small_sorted_list.append(nums[index])
          next_expected_num = nums[index] + 1

          if index == nums_size-1 or next_expected_num != nums[index+1]:
            small_list_str = self.convert_summary_list(small_sorted_list)
            ans.append(small_list_str)
            small_sorted_list = []
        return ans

    def convert_summary_list(self, small_sorted_list: List[int]) -> str:
        """
        translate List[int] to string "a -> b"
        Args:
            small_sorted_list (List[int]): list of sorted list(int)

        Returns:
            str: traced sorted list to string (e.g. 1 -> 3)
        """
        if not small_sorted_list:
          return ""
        if len(small_sorted_list) == 1:
          return str(small_sorted_list[0])
        else:
          return str(small_sorted_list[0]) + "->" + str(small_sorted_list[-1])

#--------TEST CASES------------------------------------------------
@pytest.fixture
def solution():
  return Solution()

def test_summary_ranges(solution):
    """_summary_

    Args:
        solution (_type_): _description_
    """
    #Example1
    nums = [0,1,2,4,5,7]
    assert solution.summaryRanges(nums) == ["0->2","4->5","7"]
    #Example2
    nums = [0,2,3,4,6,8,9]
    assert solution.summaryRanges(nums) == ["0","2->4","6","8->9"]

def test_convert_summary_list(solution):
  assert solution.convert_summary_list([0]) == "0"
  assert solution.convert_summary_list([0,1,2]) == "0->2"
  assert solution.convert_summary_list([]) == ""