import collections
class Solution:
    def minimumPushes(self, word: str) -> int:
        count = collections.Counter(word)
        sortCount = sorted(count.values(),key=lambda x: x,reverse=True)
        print(sortCount)
        pushTimes = 0
        for i in range(len(sortCount)):
            pushTimes += (i//8+1) * sortCount[i]
        return pushTimes

word = "aabbccddeeffgghhiiiiii"
print(Solution().minimumPushes(word))