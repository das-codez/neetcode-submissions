# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        lenList = 0
        while temp:
            lenList+=1
            temp = temp.next
        
        num = lenList - n 
        if num == 0:
            return head.next
        temp = head
        trail = temp
        for i in range(num):
            trail = temp
            temp = temp.next
        trail.next = trail.next.next
        return head
