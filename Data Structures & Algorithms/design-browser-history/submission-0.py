class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.head.next = ListNode(url, prev=self.head)
        self.head = self.head.next

    def back(self, steps: int) -> str:
        for _ in range(steps): 
            if self.head.prev is None or self.head.prev.val is None: break
            self.head = self.head.prev
        return self.head.val

    def forward(self, steps: int) -> str:
        for _ in range(steps): 
            if self.head.next is None or self.head.next.val is None: break
            self.head = self.head.next
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)