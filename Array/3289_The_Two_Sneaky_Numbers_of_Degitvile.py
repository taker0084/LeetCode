from typing import List

# 複数あるか数えるにはdictが最適
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_dict={}
        output=[]
        for i in nums:
            if i in num_dict:
                num_dict[i]+=1
            else:
                num_dict[i]=1
        for i in num_dict:
            if num_dict[i]>1:
                output.append(i)
        return output

nums=[0,1,1,0]
print(Solution().getSneakyNumbers(nums))