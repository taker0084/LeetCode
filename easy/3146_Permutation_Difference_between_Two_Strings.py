class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0
        s_dict={}
        t_dict={}
        for i in range(len(s)):
            s_dict[s[i]] = i
            t_dict[t[i]] = i
        for i in s_dict:
            count += abs(s_dict[i] - t_dict[i])
        return count

s= "abc"
t = "bac"
print(Solution().findPermutationDifference(s, t))