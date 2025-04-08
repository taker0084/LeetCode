import pytest
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        This function needs two string, s and t.
        if s is t's subsequence, return True. otherwise, return false

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        # if s == "", s is always t's subsequence
        if s == "":
            return True
        s_char_index=0
        for char in t:
            if char == s[s_char_index]:
              s_char_index += 1
            if s_char_index==len(s):
                return True
        return False
#-----------TEST CASE----------------
@pytest.fixture
def solution():
    return Solution()

def test_isSubsequence(solution):
    """
    Test case to verify that the isSubsequence function returns the correct output

    Example1: true case
    Example2: false case
    """
    # Example1
    assert solution.isSubsequence("abc", "ahbgdc") == True
    # Example2
    assert solution.isSubsequence("axc", "ahbgdc") == False