from collections import deque

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.dct = {}
        self.maxfr = 0

    def push(self, el: int) -> None:
        if el in self.freq:
            self.freq[el] += 1
        else:
            self.freq[el] = 1
        f = self.freq[el]
        if f > self.maxfr:
            self.maxfr = f
        if f not in self.dct:
            self.dct[f] = deque()
        self.dct[f].append(el)

    def pop(self) -> int:
        el = self.dct[self.maxfr].pop()
        self.freq[el] -= 1
        if not self.dct[self.maxfr]:
            del self.dct[self.maxfr]
            self.maxfr -= 1
        return el





# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()