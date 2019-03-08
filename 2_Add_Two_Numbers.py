# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:      
        firstNode = ListNode((l1.val + l2.val)%10)
        retenue = (l1.val + l2.val)//10
        l1 = l1.next
        l2 = l2.next
        currentNode = firstNode
        while l1 or l2:
            localSum = retenue
            if l1: 
                localSum += l1.val
                l1 = l1.next
            if l2: 
                localSum += l2.val
                l2 = l2.next
            currentNode.next = ListNode(localSum%10)
            retenue = localSum//10
            currentNode = currentNode.next
        if retenue:
            currentNode.next = ListNode(retenue)
        return firstNode
        