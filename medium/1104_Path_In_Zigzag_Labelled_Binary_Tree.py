from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans=[]
        while label>0:
          ans.append(label)
          label//=2
        ans.reverse()
        length=len(ans)
        for i in range(length):
          if i%2==0:
            ans[i]=2**(i+1)-1-ans[i]+2**i
        print(ans)

label=26
print(Solution().pathInZigZagTree(label))