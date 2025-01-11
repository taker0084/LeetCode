class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for i in range(10)]
        count=0
        for i in range(1,len(rings),2):
            num = int(rings[i])
            rods[num].add(rings[i-1])
        for ring in rods:
            if len(ring)==3:
                count+=1
        return count

rings = "B0B6G0R6R0R6G9"
print(Solution().countPoints(rings))