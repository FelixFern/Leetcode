# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedSorted = None
        head = mergedSorted
        while True:
            minVal, minIdx = None, None
            noneCount = 0
            for idx, val in enumerate(lists):
                if(val == None):
                    noneCount += 1 
                elif(minVal == None):
                    minVal, minIdx = val.val, idx 
                elif(minVal > val.val):
                    minVal, minIdx = val.val, idx 

            if(noneCount == len(lists)):
                break
            else: 
                lists[minIdx] = lists[minIdx].next

            if(mergedSorted == None):
                mergedSorted = ListNode(minVal)
                head = mergedSorted
            else: 
                nextHead = head
                nextHead.next = ListNode(minVal)
                head = nextHead.next

        return mergedSorted