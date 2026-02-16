# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        moving = head
        n = 0

        while moving:
            n += 1
            moving = moving.next

        for i in range(n // 2):
            head = head.next

        return head
