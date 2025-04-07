class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        length_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length_needle] == needle:
                return i