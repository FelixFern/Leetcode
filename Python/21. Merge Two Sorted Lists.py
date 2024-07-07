# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if (l1 != None or l2 != None):
            res_list = ListNode()
            current = res_list
            print('test')

            while l1 != None or l2 != None:
                if (l1 == None):
                    current.val = l2.val
                    l2 = l2.next
                elif (l2 == None):
                    current.val = l1.val
                    l1 = l1.next
                elif (l1.val >= l2.val):
                    current.val = l2.val
                    l2 = l2.next
                elif (l2.val > l1.val):
                    current.val = l1.val
                    l1 = l1.next
                if (l1 != None or l2 != None):
                    current.next = ListNode()
                    current = current.next

            return res_list

        return
