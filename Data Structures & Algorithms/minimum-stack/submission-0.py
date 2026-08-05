class MinStack:
    def __init__(self):
        self.min = 0
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        diff = self.stack.pop()
        # If difference was negative, restore the previous minimum
        if diff < 0:
            self.min -= diff

    def top(self) -> int:
        diff = self.stack[-1]
        # If diff > 0, actual value is diff + min; otherwise value is cur min
        return diff + self.min if diff > 0 else self.min

    def getMin(self) -> int:
        return self.min