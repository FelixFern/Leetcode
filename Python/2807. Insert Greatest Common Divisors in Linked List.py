# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        tempGCD = []

        def gcd(a,b):
            if (b == 0):
                return a
            return gcd(b, a % b)

        node = head
        while True:
            if(node == None):
                break
            temp.append(node.val)
            node = node.next

        for i in range(len(temp) - 1):
            tempGCD.append(gcd(temp[i], temp[i + 1]))

        count = 0

        res = None
        head = res
        for i in range(len(temp) + len(tempGCD)):
            if(i % 2 == 0):
                tempNode = ListNode(temp[i // 2])
                if(i == 0):
                    res = tempNode
                    head = res
                else:
                    nextNode = head
                    nextNode.next = tempNode
                    head = nextNode.next
            else:
                tempNode = ListNode(tempGCD[i // 2])
                nextNode = head
                nextNode.next = tempNode
                head = nextNode.next
        return res