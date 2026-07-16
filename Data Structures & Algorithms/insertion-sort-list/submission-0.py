# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # Dummy node for sorted list
        curr = head

        while curr:
            prev = dummy

            # Find the correct position to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Store next node before changing links
            next_node = curr.next

            # Insert current node
            curr.next = prev.next
            prev.next = curr

            # Move to next node
            curr = next_node

        return dummy.next