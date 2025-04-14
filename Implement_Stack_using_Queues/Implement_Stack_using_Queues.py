class Queue:
    def __init__(self):
        self.data = []

    def push_q(self, x):
        self.data.append(x)

    def pop_q(self):
        return self.data.pop(0)

    def peek_q(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


class MyStack:

    def __init__(self):
        self.first = Queue()
        self.second = Queue()

    def push(self, x: int) -> None:
        self.second.push_q(x)
        while not self.first.is_empty():
            self.second.push_q(self.first.pop_q())
        self.first, self.second = self.second, self.first

    def pop(self) -> int:
        return self.first.pop_q()

    def top(self) -> int:
        return self.first.peek_q()

    def empty(self) -> bool:
        return self.first.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()