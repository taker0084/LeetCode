from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        out=[0]*n
        out[0]=pref[0]
        for i in range(1,n):
            out[i]=pref[i-1]^pref[i]
        return out
      
pref=[5,2,0,3,1]
print(Solution().findArray(pref))