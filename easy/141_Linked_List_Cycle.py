from typing import Optional

import pytest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        checked_node = set()
        while head:
            if head in checked_node:
                return True
            else:
                checked_node.add(head)
                head = head.next
        return False

#-------------------TEST CASES-------------------
@pytest.fixture
def solution():
    return Solution()

def test_hasCycle(solution):
    # Test case 1: No cycle
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert solution.hasCycle(head) == False
    
    # Test case 2: Cycle
    head.next.next.next = head.next
    assert solution.hasCycle(head) == True
    
    # Test case 3: Empty list
    assert solution.hasCycle(None) == False