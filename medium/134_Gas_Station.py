from turtle import st
from typing import List
import pytest


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        this function returns a start index of this circuit

        Args:
            gas (List[int]): a amount of gas we can get at the station
            cost (List[int]): a cost of gas we move to

        Returns:
            int: an index of stations[i]
        """
        if sum(gas) < sum(cost):
            return -1
        tank, idx = 0, 0
        for i in range(len(gas)):
          tank += gas[i] - cost[i]
          if tank < 0:
            tank = 0
            idx = i + 1
        return idx

    #     start_positions = self.start_position(gas, cost)
    #     diff_list = self.diff_list(gas, cost)
    #     if start_positions == -1:
    #         return -1
    #     for start in start_positions:
    #         if self.can_travel(diff_list, start):
    #             return start
    #     return -1
    
    # def start_position(self, gas: List[int], cost: List[int]) -> List[int]:
    #     start_positions = []
    #     for i in range(len(gas)):
    #         if gas[i] >= cost[i]:
    #             start_positions.append(i)
    #     if len(start_positions)>=1:
    #         return start_positions
    #     return -1
    
    # def diff_list(self, gas: List[int], cost: List[int]) -> List[int]:
    #     diff_list = []
    #     for i in range(len(gas)):
    #         diff_list.append(gas[i] - cost[i])
    #     return diff_list
    
    # def can_travel(self, diff_list: List[int], start: int) -> bool:
    #     tank = 0
    #     for i in range(len(diff_list)):
    #         tank += diff_list[(start + i) % len(diff_list)]
    #         if tank < 0:
    #             return False
    #     return True
    
#--------------TEST CASES------------------
@pytest.fixture
def solution():
  return Solution()

def test_canCompleteCircuit(solution):
    """
    Example1: normal success
    Example2: normal failure
    """
    # Example1
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    expected = 3
    assert solution.canCompleteCircuit(gas, cost) == expected
    # Example2
    gas = [2,3,4]
    cost = [3,4,3]
    expected = -1
    assert solution.canCompleteCircuit(gas, cost) == expected
