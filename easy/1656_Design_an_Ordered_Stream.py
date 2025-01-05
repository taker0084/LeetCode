from typing import List


class OrderedStream:
  
    def __init__(self, n: int):
        self.Stream = [None]*(n+2)
        self.place = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.Stream[idKey]=value
        if self.place == idKey:
            while self.Stream[self.place] is not None:
                self.place += 1
            return self.Stream[idKey:self.place]
        return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)