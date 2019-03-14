# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = []
        values = [(l.val,i) for i,l in enumerate(lists) if l]
        values = sorted(values)
        while values:
            out = values.pop(0)
            result.append(out[0])
            if lists[out[1]].next:
                lists[out[1]] = lists[out[1]].next
                new_tuple = (lists[out[1]].val, out[1])
                i = 0
                for i,value in enumerate(values):
                    if value[0] > new_tuple[0]:
                        values.insert(i, new_tuple)
                        break
                else:
                    values.insert(i+1, new_tuple)
        return result