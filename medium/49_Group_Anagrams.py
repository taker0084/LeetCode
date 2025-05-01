import collections
from typing import List
import pytest
from returns.result import Success, Failure


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The groupAnagrams function takes a list of strings and groups them into anagrams.
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.

        Args:
            strs (List[str]): A list of strings that may contain anagrams.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains strings that are anagrams of each other.
            If the input list is empty, it returns an empty list.
        """
        if not strs:
            return Success([])
        if len(strs) == 1:
            return Success([strs])
        anagram_dict = collections.defaultdict(list)
        for sentence in strs:
            sorted_sentence = ''.join(sorted(sentence))
            anagram_dict[sorted_sentence].append(sentence)
        return Success(list(anagram_dict.values()))
#-------------------TEST CASES----------------
@pytest.fixture
def solution():
    return Solution()
def test_groupAnagrams(solution):
    """
    Example 1: normal input
    Example 2: empty input
    Example 3: single input
    """
    #Example1
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    result = solution.groupAnagrams(strs)
    assert result.unwrap() == expected

    #Example2
    strs = [""]
    expected = [[""]]
    result = solution.groupAnagrams(strs)
    assert result.unwrap() == expected

    #Example3
    strs = ["a"]
    expected = [["a"]]
    result = solution.groupAnagrams(strs)
    assert result.unwrap() == expected