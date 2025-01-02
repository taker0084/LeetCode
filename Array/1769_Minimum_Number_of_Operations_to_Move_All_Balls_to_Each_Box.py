from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        pref = p = s = 0
        for i, el in enumerate(boxes):
            if el == '1':
                pref += i  #boxes[0]に持ってくるのに何回操作が必要か
                p += 1     #ボールの数
        for el in boxes:
            answer.append(pref)  #最初は全てboxes[0]に持ってくる
            if el == '1':
                p -= 1                  #残りの球数を１引く
                s += 1                  #新たに移動させる球
            pref = pref - p + s    #現在の累積コストから残りのボールの数を引き、移動したボールの数を加えます?
        return answer

        # out = []
        # boxes = [int(isBallExist) for isBallExist in boxes]
        # for i in range(len(boxes)):
        #     count = 0
        #     for j in range(len(boxes)):
        #         if i != j and boxes[j] == 1:
        #             count += abs(i - j)
        #     out.append(count)
        # return out

boxes = "110"
print(Solution().minOperations(boxes))