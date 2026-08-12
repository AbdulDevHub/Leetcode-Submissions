class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)        # val -> frequency
        self.stacks = defaultdict(list)     # frequency -> stack of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        self.max_freq = max(self.max_freq, f)
        self.stacks[f].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq[val] -= 1
        # If highest frequency stack becomes empty, lower max frequency pointer
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return val
