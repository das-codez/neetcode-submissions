# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2
        head = node = ListNode()
        while a and b:
            if a.val > b.val:
                node.next = b
                
                b = b.next
            else:
                node.next = a
                a = a.next
            node = node.next

        node.next = a or b
        return head.next