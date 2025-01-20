# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = head
        for i in range(n):
            node = node.next
        # node 指向正数第 n + 1 个节点, dummy 指向第 0 个节点，dummy.next 指向第 1 个节点
        # loop invariants: dummy.next 指向以 node 向前数的第 n 个节点
        while node is not None:
            dummy = dummy.next
            node = node.next
        if dummy.next == head:
            return head.next
        dummy.next = dummy.next.next
        return head