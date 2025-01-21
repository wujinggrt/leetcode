# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, head)
        dummy = node
        while node.next is not None and node.next.next is not None:
            # swap the pair after the node
            former = node.next
            latter = former.next
            nextPair = latter.next
            node.next = latter
            former.next = nextPair
            latter.next = former
            node = former
        return dummy.next
