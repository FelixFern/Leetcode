# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''

        num1_node = l1
        num2_node = l2

        while True:
            if (num1_node is not None):
                num1 = str(num1_node.val) + num1
                num1_node = num1_node.next
            else:
                break
        while True:
            if (num2_node is not None):
                num2 = str(num2_node.val) + num2
                num2_node = num2_node.next
            else:
                break

        res = str(int(num1) + int(num2))

        curr_nodes = ListNode()

        for i, val in enumerate(res):
            prev_nodes = ListNode(val=curr_nodes.val, next=curr_nodes.next)
            curr_nodes.val = val
            if i != 0:
                curr_nodes.next = prev_nodes

        return (curr_nodes)
