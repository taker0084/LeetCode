import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        words = s.split()
        s = "".join(words).lower()
        return s[::-1] == s