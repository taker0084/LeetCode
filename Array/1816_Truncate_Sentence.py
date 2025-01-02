class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        truncated_words = words[:k]
        out=""
        for word in truncated_words:
            out+=word+" "
        return out.strip()

s = "Hello how are you Contestant"
k = 4
print(Solution().truncateSentence(s,k))