class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

# Step-by-Step Execution Example
# s = MyStack()
# s.push(10)  # self.q = deque([10, None])
# s.push(20)  # self.q = deque([20, deque([10, None])])

# s.top()     # Returns 20 (looks at self.q[0])
# s.pop()     # Pops 20, sets self.q = deque([10, None]), returns 20
# s.empty()   # Returns False (self.q is not None)