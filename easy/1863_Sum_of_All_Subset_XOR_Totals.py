from typing import List
import collections


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        counter=0
        dp=collections.Counter()
        dp[0]=1
        for num in nums:
            for mask, count in tuple(dp.items()):  # dpのアイテムをタプルに変換
                dp[num ^ mask] += count  # numを使って新しい部分集合を作成
        for mask,count in tuple(dp.items()):
            counter+=mask*count
        return counter
        
nums=[3,4,5,6,7,8]
print(Solution().subsetXORSum(nums))