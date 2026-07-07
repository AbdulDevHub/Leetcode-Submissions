class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class RandomizedSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**6)]
        self.usedBucket = []

    def insert(self, val: int) -> bool:
        cur = self.set[val % len(self.set)]
        while cur.next:
            if cur.next.val == val:
                return False
            cur = cur.next
        cur.next = ListNode(val)
        self.usedBucket.append(val % len(self.set))
        return True

    def remove(self, val: int) -> bool:
        cur = self.set[val % len(self.set)]
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.usedBucket.remove(val % len(self.set))
                return True
            cur = cur.next
        return False

    def getRandom(self) -> int:   
        cur = self.set[random.choice(self.usedBucket)]
        bucketIndexCounter = random.randint(1, 10)
        while cur.next and bucketIndexCounter != 0:
            cur = cur.next
        return cur.val

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()