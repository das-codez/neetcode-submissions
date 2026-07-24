"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = {None:None}
        curr = head
        while curr:
            new_list[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = new_list[curr]
            copy.next = new_list[curr.next]
            copy.random = new_list[curr.random]
            curr = curr.next
        return new_list[head]
