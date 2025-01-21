# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l: Optional[ListNode], m: Optional[ListNode]) -> Optional[ListNode]:
        n = ListNode()
        ret = n
        while l is not None and m is not None:
            if l.val < m.val:
                n.next = l
                l = l.next
            else:
                n.next = m
                m = m.next
            n = n.next
            n.next = None
        while l is not None:
            n.next = l
            l = l.next
            n = n.next
            n.next = None
        while m is not None:
            n.next = m
            m = m.next
            n = n.next
            n.next = None
        return ret.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 2:
            return lists[0] if len(lists) == 1 else None
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        l, r = 0, len(lists)
        m = l + (r - l) // 2
        mergedLeft = self.mergeKLists(lists[l:m])
        mergedRight = self.mergeKLists(lists[m:r])
        return self.merge(mergedLeft, mergedRight)