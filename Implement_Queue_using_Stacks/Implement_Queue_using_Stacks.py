class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


class MyQueue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def push(self, x: int) -> None:
        self.first.push(x)

    def pop(self) -> int:
        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())
        return self.second.pop()

    def peek(self) -> int:
        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())
        return self.second.peek()

    def empty(self) -> bool:
        return self.first.empty() and self.second.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()