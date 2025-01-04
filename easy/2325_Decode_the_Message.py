class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict={}
        for i in range(len(key)):
            if key[i] not in dict and key[i]!=' ':
                dict[key[i]]=chr(97+len(dict))
        out = ""
        for i in message:
            if i==' ':
                out+=' '
            else:
                out+=dict[i]
        return out

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(Solution().decodeMessage(key,message))