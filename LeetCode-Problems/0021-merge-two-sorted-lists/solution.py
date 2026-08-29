class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head node to simplify list building
        dummy = ListNode(0)
        tail = dummy
        
        # Traverse while both lists have elements
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Attach whichever list still has remaining elements
        tail.next = list1 if list1 else list2
        
        # Return the head of the merged list (skipping dummy)
        return dummy.next
