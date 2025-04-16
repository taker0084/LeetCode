import collections
from typing import List

import pytest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        three sum returns a list of numbers that their sum is equal to 0

        Args:
            nums (List[int]): _description_

        Returns:
            List[List[int]]: _description_
        """
        sorted_nums = sorted(nums)
        ans = set()
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if sum == 0:
                    ans.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return list(ans)
#---------------TEST CASES-------------------------
@pytest.fixture
def solution():
    return Solution()

def test_threeSum():
    """
    Example1: normal input
    """
    #Example1
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [(-1,0,1),(-1,-1,2)]