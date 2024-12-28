import collections
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise=0
        count=0
        for num in nums:
            max_bitwise|=num
        dp=collections.Counter()
        dp[0]=1
        # 動的計画法
        # dp[0]=1として初期値を設定
        # maskは今まで計算した全てのbitwiseの値を指す
        # 計算済の全通りのbitwiseに対して、nums[i]を加えた場合のbitwiseを計算し、その結果のdp[bitwise]に+1
        for num in nums:
            for mask, count in tuple(dp.items()):  # dpのアイテムをタプルに変換
                dp[num | mask] += count  # numを使って新しい部分集合を作成
        return dp[max_bitwise]  # maxOrのカウントを返す
        

nums=[2,2,2]
print(Solution().countMaxOrSubsets(nums))
    
    

