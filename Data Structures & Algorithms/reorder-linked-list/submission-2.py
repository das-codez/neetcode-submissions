# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start_second = slow.next
        prev = slow.next = None
        while start_second:
            temp = start_second.next
            start_second.next = prev
            prev = start_second
            start_second = temp
        first, start_second = head, prev
        while start_second:
            tmp1, tmp2 = first.next, start_second.next
            first.next = start_second
            start_second.next = tmp1
            first, start_second = tmp1, tmp2
        