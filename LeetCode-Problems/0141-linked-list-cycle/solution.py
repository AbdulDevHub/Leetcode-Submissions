# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        seen = set() # Use set for O(1) lookups
        while temp:
            if temp in seen: return True
            seen.add(temp)
            temp = temp.next
        return False
