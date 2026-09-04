class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        cur = self.head
        for _ in range(index): cur = cur.next
        return cur

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        prev = self.getPrev(index)
        node = ListNode(val, prev.next)
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: return
        prev = self.getPrev(index)
        prev.next = prev.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)