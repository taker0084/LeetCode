from typing import List

import pytest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        this function needs a list of integers and returns List

        Args:
            nums (List[int]): a list of integers

        Returns:
            List[int]: an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        """
        all_products = 1
        zero_count = 0
        for i in range( len(nums)):
            all_products *= nums[i]
            if nums[i] == 0:
                zero_count += 1
        if zero_count >= 2:
            return [0] * len(nums)
        ans = [1] * len(nums)
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    ans[i] = all_products
                else:
                    ans[i] = 0
            else:
                ans[i] = all_products // nums[i]
        return ans
#------------------TEST CASES------------------
@pytest.fixture
def solution():
  return Solution()

def test_productExceptSelf(solution):
    nums = [1,2,3,4]
    expected = [24,12,8,6]
    assert solution.productExceptSelf(nums) == expected