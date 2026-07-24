# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        curr = l1
        while curr:
            stack1.append(str(curr.val))
            curr = curr.next
        curr = l2
        while curr:
            stack2.append(str(curr.val))
            curr = curr.next
        number1, number2 = "".join(reversed(stack1)), "".join(reversed(stack2))
        total = int(number1) + int(number2)
        total = reversed(str(total))
        dummy  = ListNode(0)
        curr = dummy
        for c in total:
            curr.next = ListNode(int(c))
            curr = curr.next
        return dummy.next