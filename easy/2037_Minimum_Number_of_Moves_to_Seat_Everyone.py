from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move=0
        for i in range(len(seats)):
            move+=abs(seats[i]-students[i])
        return move

seats =  [3,1,5]
students=[2,7,4]
print(Solution().minMovesToSeat(seats,students))