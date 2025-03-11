from typing import List
import collections

import pytest

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        get importance sum of employee and all subordinates

        Args:
            employees (List['Employee']): all employee list
            id (int): employee's id

        Returns:
            int: all profit of employee[id]
        """
        if not employees:
            return 0
        employees_dict = self.make_employee_dictionary(employees)

        def dfs(node):
          total_importance = 0
          if not node:
            return 0

          for sub in node.subordinates:
            sub_employee = employees_dict[sub]
            total_importance += dfs(sub_employee)

          if node.id == id:
            return node.importance + total_importance

          return total_importance + node.importance

        return dfs(employees_dict[id])

    def make_employee_dictionary(self, employees) -> dict:
      """
      make employees' dict by their list

      Args:
          employees (_type_): an item in employees

      Returns:
          dict: employees' list
      """
      employee_dict = collections.defaultdict(Employee)
      for employee in employees:
        employee_dict[employee.id] = employee
      return employee_dict
#-----Test Code-----
@pytest.fixture
def solution():
  return Solution()
def test_getImportance(solution):
  #example1
  employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, [])
  ]
  assert solution.getImportance(employees, 1) == 11
  #example2
  employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, [4]),
    Employee(3, 4, []),
    Employee(4, 1, [])
  ]
  assert solution.getImportance(employees, 1) == 13