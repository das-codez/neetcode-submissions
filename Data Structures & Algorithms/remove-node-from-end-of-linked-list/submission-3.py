# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next
        dummy = ListNode(0, head)
        trail = dummy
        while fast:
            fast = fast.next
            trail = trail.next
            
        trail.next = trail.next.next
        return dummy.next
