from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        separation=0
        ans=[]
        for i in range(len(s)):
            if last[s[i]] > separation:
                separation = last[s[i]]
            if i == separation:
                ans.append(i+1 - sum(ans))
        return ans


s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))