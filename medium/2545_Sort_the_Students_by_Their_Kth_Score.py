from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        #lambdaは関数名を定義せずとも関数を作成できる
        #key引数にlambda関数を設定することによって、任意の方法でソートをすることができる
        sortKScores = sorted(score, key=lambda x: x[k], reverse=True)
        return sortKScores

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(Solution().sortTheStudents(score,k))