import collections
from typing import List

import pytest


class ThroneInheritance:
#TODO add comments
    def __init__(self, kingName: str):
        """
        self.count_parent_child: a list of parent-child pair
        self.death_list: a list of dead ancestor

        Args:
            kingName (str): first ancestor name
        """
        self.king_name = kingName
        self.count_parent_child = collections.defaultdict(list)
        self.death_list = set()

    def birth(self, parentName: str, childName: str) -> None:
        """
        add child to parent

        Args:
            parentName (str): parent name
            childName (str): child name
        """
        self.count_parent_child[parentName].append(childName)

    def death(self, name: str) -> None:
        """
        add name to death list

        Args:
            name (str): dead person's name
        """
        self.death_list.add(name)

    def getInheritanceOrder(self) -> List[str]:
        """
        get inheritance order

        Returns:
            List[str]: a list of inheritance order
        """
        self.inheritance_order = []
        self.make_inheritance_order(self.king_name)
        return self.inheritance_order

    def make_inheritance_order(self, parent: str) -> None:
        """
        make inheritance order

        Args:
            parent (str): parent name
        """
        if parent not in self.death_list:
            self.inheritance_order.append(parent)
        for child in self.count_parent_child[parent]:
            self.make_inheritance_order(child)
#------------TEST CASES----------------
@pytest.fixture
def solution():
    return ThroneInheritance
def test(solution):
    """
      Example1: child birth test
      Example2: child death test
      Example3: grandchild birth test
      Example4: grandchild death test
    """
    #Example1
    solution = ThroneInheritance("king")
    solution.birth("king", "andy")
    solution.birth("king", "bob")
    assert solution.getInheritanceOrder() == ["king", "andy", "bob"]
    #Example2
    solution = ThroneInheritance("king")
    solution.birth("king", "catherine")
    solution.birth("king", "matthew")
    solution.death("catherine")
    assert solution.getInheritanceOrder() == ["king", "matthew"]
    #Example3
    solution = ThroneInheritance("king")
    solution.birth("king", "catherine")
    solution.birth("catherine", "matthew")
    solution.birth("king", "bob")
    assert solution.getInheritanceOrder() == ["king", "catherine", "matthew", "bob"]
    #Example4
    solution = ThroneInheritance("king")
    solution.birth("king", "catherine")
    solution.birth("catherine", "matthew")
    solution.birth("king", "bob")
    solution.death("matthew")
    assert solution.getInheritanceOrder() == ["king", "catherine", "bob"]