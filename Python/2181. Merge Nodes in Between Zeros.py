# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        res = []
        sums = 0
        while temp:
            if(temp.val == 0 and sums != 0): 
                res.append(sums)
                sums = 0
            else: 
                sums += temp.val
            temp = temp.next 

        res_node = ListNode(res[0])
        current = res_node

        for i in res[1:]:
            new_node = ListNode(i)
            current.next = new_node
            current = current.next

        return res_node