from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for hour in hours:
            if hour>=target:
                count+=1
        return count

hours=[0,1,2,3,4]
target=2
print(Solution().numberOfEmployeesWhoMetTarget(hours,target))