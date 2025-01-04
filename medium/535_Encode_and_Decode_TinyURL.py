import random
import string


class Codec:
    character = string.ascii_letters + string.digits
    BASEURL = "http://tinyurl.com/"
    def __init__(self):
        self.urlMap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = ''.join(random.choice(self.character) for i in range(6))
        self.urlMap[code] = longUrl
        return self.BASEURL + code;

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split('/')[-1]
        return self.urlMap[code]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

longUrl = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.encode(longUrl))
print(codec.decode(codec.encode(longUrl)))