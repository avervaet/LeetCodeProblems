# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next_node = head.next
        head.next = next_node.next
        next_node.next = head
        first = next_node
        current = head
        while current.next:
            next_node = current.next
            if not next_node.next:
                break
            current.next = next_node.next
            current = next_node
            next_node = current.next
            current.next = next_node.next
            next_node.next = current
        return first