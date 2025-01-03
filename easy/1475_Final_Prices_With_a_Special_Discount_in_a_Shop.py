from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      result=[]
      for i in range(len(prices)):
        ischeck=False
        for j in range(i+1,len(prices)):
          if prices[i]>=prices[j]:
            ischeck=True
            print(prices[i],prices[j])
            result.append(prices[i]-prices[j])
            break
        if(ischeck==0):
          result.append(prices[i])
      return result

prices=[1,2,3,4,5]
print(Solution().finalPrices(prices))