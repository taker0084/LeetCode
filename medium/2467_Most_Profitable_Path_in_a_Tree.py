import collections
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        EdgeList = collections.defaultdict(list)
        for root, edge in edges:
            EdgeList[root].append(edge)
            EdgeList[edge].append(root)

        # ボブの経路探索 (DFS)
        visited = set()
        bob_path = {}

        def dfs(node, time):
            visited.add(node)
            bob_path[node] = time
            if node == 0:
                return True
            for next_node in EdgeList[node]:
                if next_node not in visited and dfs(next_node, time+1):
                    return True

            bob_path.pop(node, None)
            return False
        dfs(bob, 0)

        visited = set()
        queue = collections.deque([(0, 0, 0)])  # (node, level, profit)
        max_cost = float('-inf')

        def bfs(node, level, profit):
            nonlocal max_cost
            if node not in bob_path or level < bob_path[node]:
                profit += amount[node]
            elif bob_path[node] == level:
                profit += amount[node]//2

            visited.add(node)

            if len(EdgeList[node])==1 and node != 0:
                max_cost = max(max_cost, profit)
                return

            for next_node in EdgeList[node]:
                if next_node not in visited:
                    bfs(next_node, level + 1, profit)

        bfs(0, 0, 0)
        return max_cost

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
print(Solution().mostProfitablePath(edges, bob, amount))