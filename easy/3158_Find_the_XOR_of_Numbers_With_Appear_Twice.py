from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        setNum = set()
        ans = 0
        for num in nums:
            if num in setNum:
                ans ^= num
            else:
                setNum.add(num)
        return ans

nums = [1,2,1,2]
print(Solution().duplicateNumbersXOR(nums))