class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)
        
        # print("push", self.stack)
        
    def pop(self) -> None:
        self.stack.pop()
        # print("pop", self.stack)
        self.minStack.pop()

    def top(self) -> int:
        # print("top", self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        # print("getMin", self.stack)
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# -2 -2, 0 -2, -3 -3