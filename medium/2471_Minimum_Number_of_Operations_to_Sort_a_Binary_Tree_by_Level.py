# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr: List[int]) -> int:
            n = len(arr)
            # 元のリストとその添字番号を保存
            indexed_arr = [(val, i) for i, val in enumerate(arr)]
            indexed_arr.sort()  # Sort by value
            # その添字番号が訪問されたかどうか
            visited = [False] * n
            swaps = 0

            for i in range(n):
                # 各添字番号について、並び替えた後と元の位置が同じ位置ならスキップ
                if visited[i] or indexed_arr[i][1] == i:
                    continue

                cycle_size = 0
                x = i

                #訪問済みでない場合
                while not visited[x]:
                    #訪問済みにする
                    visited[x] = True
                    #元の添字番号に移動
                    x = indexed_arr[x][1]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        queue=deque([root])
        count=0
        while queue:
            queue_size=len(queue)
            values=[]
            for _ in range(queue_size):
                node=queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            count += min_swaps_to_sort(values)

        return count