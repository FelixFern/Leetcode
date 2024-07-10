# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head != None):
            res_node = ListNode(head.val)
            res_current = res_node
            current = head.next
            while current != None:
                if(current.val != res_current.val): 
                    new_node = ListNode(current.val)
                    res_current.next = new_node
                    res_current = res_current.next
                current = current.next 

            return res_node
        return