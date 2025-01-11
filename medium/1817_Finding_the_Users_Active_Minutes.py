import collections
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        dict = collections.defaultdict(set)
        for log in logs:
            dict[log[0]].add(log[1])
        for value in dict.values():
            ans[len(value)-1] += 1
        return ans

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(Solution().findingUsersActiveMinutes(logs, k))