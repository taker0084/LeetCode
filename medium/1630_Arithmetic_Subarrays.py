from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        out = []
        for queryLength in range(len(l)):
            subArray = nums[l[queryLength]:r[queryLength]+1]
            subArray.sort()
            print(subArray)
            diff = subArray[1] - subArray[0]
            for i in range(2, len(subArray)):
                if subArray[i] - subArray[i-1] != diff:
                    out.append(False)
                    break
            else:
                out.append(True)
        return out

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
print(Solution().checkArithmeticSubarrays(nums,l,r))
