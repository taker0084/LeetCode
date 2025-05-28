import pytest
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        The simplifyPath function simplifies a given file path by removing
        unnecessary directory components.

        Args:
            path (str): The input file path to be simplified.

        Returns:
            str: The simplified file path.
        """
        if not path:
            return ""
        path_args = path.split('/')
        ans_list = []
        for arg in path_args:
            if arg == "" or arg == ".":
                continue
            elif arg == '..':
                if ans_list:
                    ans_list.pop()
                else:
                    continue
            else:
                ans_list.append(arg)
        return "/" + "/".join(ans_list)
#-------------------TEST CASES-------------------
@pytest.fixture
def solution():
    return Solution()

def test_simplifyPath(solution):
    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/home//foo/") == "/home/foo"