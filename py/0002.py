from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     cur = dummy = ListNode()
    #     carry = 0
    #     while l1 or l2 or carry:
    #         if l1:
    #             carry = carry+l1.val
    #             l1 = l1.next
    #         if l2:
    #             carry = carry+l2.val
    #             l2 = l2.next
    #         cur.next = ListNode(carry%10)
    #         carry = carry//10
    #         cur = cur.next
    #     return dummy.next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 使用进位记录相加超过9的情况。使用dummy简化结果的第一个元素判空的情况
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            carry = 0 if tmp < 10 else 1
            node = ListNode(tmp % 10)
            tail.next = node
            tail = node
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            tmp = l1.val + carry
            carry = 0 if tmp < 10 else 1
            node = ListNode(tmp % 10)
            tail.next = node
            tail = node
            l1 = l1.next
        while l2 is not None:
            tmp = l2.val + carry
            carry = 0 if tmp < 10 else 1
            node = ListNode(tmp % 10)
            tail.next = node
            tail = node
            l2 = l2.next
        if carry == 1:
            tail.next = ListNode(1)
        return dummy.next

print(ord('a'))