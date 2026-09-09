from collections import defaultdict


class ListNode:
    """Node in a doubly linked list storing cache entry data and access count."""

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1  # Initial access count upon creation
        self.prev = None
        self.next = None


class LinkedList:
    """Doubly linked list with dummy head/tail nodes for O(1) insertions/deletions.

    Maintains nodes in LRU order for a specific frequency bucket:
    - left.next is the Least Recently Used (LRU) node in this frequency.
    - right.prev is the Most Recently Used (MRU) node in this frequency.
    """

    def __init__(self):
        # Dummy boundary nodes avoid edge-case null checks during insertion/deletion
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self) -> int:
        return self.size

    def pushRight(self, node: ListNode) -> None:
        """Appends a node right before the dummy right tail (marks it as Most Recently Used)."""
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node: ListNode) -> None:
        """Removes an arbitrary node from the list in O(1) time."""
        prev, next_node = node.prev, node.next
        prev.next = next_node
        next_node.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self) -> ListNode:
        """Removes and returns the Least Recently Used node (right after dummy left head)."""
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node


class LFUCache:
    """Least Frequently Used Cache maintaining O(1) lookup, insertion, and eviction.

    Evicts the key with the lowest frequency. If a tie occurs, evicts the least
    recently used key among those with the minimum frequency.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0  # Tracks the current minimum frequency across all stored keys
        self.nodeMap = {}  # key -> ListNode reference
        self.listMap = defaultdict(
            LinkedList
        )  # frequency -> LinkedList of nodes with that frequency

    def counter(self, node: ListNode) -> None:
        """Updates a node's frequency, moving it to the next frequency list."""
        cnt = node.freq

        # Step 1: Remove node from its current frequency list
        self.listMap[cnt].pop(node)

        # Step 2: If the list at current min frequency becomes empty, increment global minimum frequency
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

        # Step 3: Increment node frequency and move it to the new frequency list (as MRU)
        node.freq += 1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        """Fetches the value for a key and increments its frequency count."""
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self.counter(node)  # Increment access count
        return node.val

    def put(self, key: int, value: int) -> None:
        """Inserts or updates a key-value pair. Evicts the LFU item if capacity is exceeded."""
        if self.cap == 0:
            return

        # Case 1: Key already exists -> Update value and increment frequency count
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        # Case 2: Cache is full -> Evict the LFU node (LRU node within lowest frequency)
        if len(self.nodeMap) == self.cap:
            lfu_node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(lfu_node.key)

        # Case 3: Insert brand new node (initial frequency = 1, min frequency resets to 1)
        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.lfuCnt = 1