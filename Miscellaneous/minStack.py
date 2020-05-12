class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            minval = self.getMin()
            actualmin = min(minval, x)
            self.stack.append((x, actualmin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
