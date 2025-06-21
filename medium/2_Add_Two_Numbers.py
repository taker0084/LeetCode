from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        this function adds two numbers represented by linked lists

        Args:
            l1 (Optional[ListNode]): first linked list
            l2 (Optional[ListNode]): second linked list

        Returns:
            Optional[ListNode]: linked list representing the sum of the two numbers
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy_head = ListNode(0)
        current_node = dummy_head
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            current_node.next = ListNode(sum % 10)
            current_node = current_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current_node.next = ListNode(carry)

        return dummy_head.next
#------------------Test Cases------------------
@pytest.fixture
def solution():
    return Solution()

def test_add_two_numbers(solution):
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8

def test_add_two_numbers_empty_lists(solution):
    l1 = None
    l2 = None
    result = solution.addTwoNumbers(l1, l2)
    assert result is None

def test_add_two_numbers_one_empty_list(solution):
    l1 = None
    l2 = ListNode(0)
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 0
    assert result.next is None

