class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        temp = []
        returnVal = self.queue[0]
        for i in range(1, len(self.queue)):
            temp.append(self.queue[i])
        self.queue = temp
        
        return returnVal

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()