class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.front_history = []

    def visit(self, url: str) -> None:
        self.back_history.append(url)
        self.front_history = []

    def back(self, steps: int) -> str:
        while steps and len(self.back_history) > 1:
            self.front_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while steps and self.front_history:
            self.back_history.append(self.front_history.pop())
            steps -= 1
        return self.back_history[-1]