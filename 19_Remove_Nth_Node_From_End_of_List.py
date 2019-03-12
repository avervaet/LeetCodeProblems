# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        result = []
        while head.next:
            result.append(head.val)
            head = head.next
        result.append(head.val)
        result.pop(len(result) - n)
        return result