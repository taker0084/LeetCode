from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        this function merges two sorted linked lists into a single sorted linked list

        Args:
            list1 (Optional[ListNode]): first sorted linked list
            list2 (Optional[ListNode]): second sorted linked list

        Returns:
            Optional[ListNode]: merged sorted linked list
        """
        dummy_node = ListNode()
        current = dummy_node
        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val <= list2.val:
              current.next = list1
              list1 = list1.next
            else:
              current.next = list2
              list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy_node.next

#------------------Test Cases------------------
@pytest.fixture
def solution():
    return Solution()

def test_merge_two_lists(solution):
    """
    Test case for merging two sorted linked lists
    Test case 1: Merging two non-empty lists
    Test case 2: Merging one empty list and one non-empty list
    Test case 3: Merging two empty lists
    """
    # Test case 1: Merging two non-empty lists
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = solution.mergeTwoLists(list1, list2)
    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4

    # Test case 2: Merging one empty list and one non-empty list
    list1 = None
    list2 = ListNode(0)
    merged_list = solution.mergeTwoLists(list1, list2)
    assert merged_list.val == 0

    # Test case 3: Merging two empty lists
    list1 = None
    list2 = None
    merged_list = solution.mergeTwoLists(list1, list2)
    assert merged_list is None
