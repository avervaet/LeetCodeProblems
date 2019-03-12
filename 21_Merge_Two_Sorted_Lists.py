# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return []
        e1 = l1.val if l1 else math.inf
        e2 = l2.val if l2 else math.inf
        if e1 < e2:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        current = start
        while l1 or l2:
            e1 = l1.val if l1 else math.inf
            e2 = l2.val if l2 else math.inf
            if e1 < e2:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        return start