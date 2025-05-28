import collections
import pytest

class MinStack:
    """
    A class that implements a stack with a minimum value.
    """

    def __init__(self):
        """
        Initialize the stack.
        """
        self.stack = collections.deque()
        self.min_stack = collections.deque()

    def push(self, val: int) -> None:
        """
        Push a value onto the stack.
        """
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Pop a value from the stack.
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        Return the top value of the stack.
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Return the minimum value of the stack.
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#-------------------TEST CASES-------------------
@pytest.fixture
def min_stack():
    return MinStack()

def test_min_stack(min_stack):
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2