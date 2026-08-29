# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newList = dummy
        temp1, temp2 = list1, list2
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val <= temp2.val: 
                    newList.next = temp1
                    temp1 = temp1.next
                else:
                    newList.next = temp2
                    temp2 = temp2.next
                newList = newList.next
            elif temp1 and not temp2:
                while temp1:
                    newList.next = temp1
                    newList = newList.next
                    temp1 = temp1.next
            else:
                while temp2:
                    newList.next = temp2
                    newList = newList.next
                    temp2 = temp2.next
        return dummy.next