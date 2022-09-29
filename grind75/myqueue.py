class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._balance_stacks()
        return self.stack2.pop(-1)

    def _balance_stacks(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

    def peek(self) -> int:
        self._balance_stacks()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack2 and not self.stack1
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
