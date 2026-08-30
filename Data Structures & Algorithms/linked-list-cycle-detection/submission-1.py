# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp:
            if hasattr(temp, 'seen'):
                return True
            temp.seen = True
            temp = temp.next
        return False
