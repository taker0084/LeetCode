from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        allLaser=0
        prev = 0
        for row in bank:
            count=row.count('1')
            if count>0:
                allLaser += count * prev
                prev = count
        return allLaser

bank = ["011001","000000","010100","001000"]
print(Solution().numberOfBeams(bank))