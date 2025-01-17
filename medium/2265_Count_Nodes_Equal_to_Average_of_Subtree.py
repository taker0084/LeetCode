# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def mean(node):
            nonlocal count
            if not node:
                return 0, 0  # 合計とノード数を返す
            
            left_sum, left_count = mean(node.left)  # 左部分木の合計とノード数
            right_sum, right_count = mean(node.right)  # 右部分木の合計とノード数
            
            total_sum = node.val + left_sum + right_sum  # 現在のノードの値を加算
            total_count = 1 + left_count + right_count  # 現在のノードをカウント
            
            # 平均を計算し、条件を満たす場合はカウントを増やす
            if node.val == total_sum // total_count:
                count += 1
            
            return total_sum, total_count  # 合計とノード数を返す

        mean(root)  # DFSを開始
        return count  # 条件を満たすノードの数を返す