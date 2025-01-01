from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        pref = p = s = 0
        for i, el in enumerate(boxes):
            if el == '1':
                pref += i
                p += 1
        for el in boxes:
            answer.append(pref)
            if el == '1':
                p -= 1
                s += 1
            pref = pref - p + s
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