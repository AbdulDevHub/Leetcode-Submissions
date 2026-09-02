# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

"""
Intuition
Use two pointers so that the gap between them is exactly n.
Move the right pointer n steps ahead first.
Then move both pointers together.
When the right pointer reaches the end, the left pointer will be just before the node we must remove.

Algorithm
1) Create a dummy node pointing to the head (helps handle deletion of the first node).
2) Set two pointers:
    - left at dummy
    - right at head
3) Move right forward n steps.
4) Move both pointers until right reaches the end.
5) Now left.next is the node to delete → skip it by doing left.next = left.next.next.
6) Return dummy.next as the updated head.
"""