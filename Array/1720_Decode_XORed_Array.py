from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out=[first]
        for i in range(len(encoded)):
            out.append(out[i]^encoded[i])
        return out

encoded = [1,2,3]
first = 1
print(Solution().decode(encoded, first))