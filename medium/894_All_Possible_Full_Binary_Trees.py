# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        #nが1なら空のノードを返す
        if n==1:
            return [TreeNode()]
        result = []
        #完全二分木はノード数が奇数 → 構造的にrootになるのは奇数番目のノード
        for i in range(1,n-1,2):
            #左部分木の全ての組み合わせ
            for j in self.allPossibleFBT(i):
                #右部分木の全ての組み合わせ
                for k in self.allPossibleFBT(n-i-1):
                    #結果をlistに追加
                    result.append(TreeNode(0, j, k))
        return result

n=7
print(Solution().allPossibleFBT(n))