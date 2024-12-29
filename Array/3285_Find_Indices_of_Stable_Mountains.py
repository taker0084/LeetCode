from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        out=[]
        for i in range(1,len(height)):
            if height[i-1] > threshold:
                out.append(i)
        return out

height = [1,2,3,4,5]
threshold = 2
print(Solution().stableMountains(height, threshold))