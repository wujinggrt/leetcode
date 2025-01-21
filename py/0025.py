# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        # 添加到新的链表
        while previous is not None:
            node = previous
            # 循环开始：node.next 指向当前 group 第一个，node 指向上一个 group 最后一个节点
            # 每轮迭代：node.next 指向当前 group，进行迭代，指导 node.next 指向下一个 group 结束
            # 循环结束：node.next 指向下个 group 第一个，node 指向当前 group 最后一个节点
            for _ in range(k):
                if node.next is None:
                    # 最后一组不足 k 个
                    return dummy.next
                node = node.next
            nextGroup = node.next
            # 断开 group
            node.next = None
            # 记录翻转链的头尾信息
            node = previous.next
            revHead = ListNode()
            revTail = node
            for _ in range(k):
                tmp = node.next
                node.next = revHead.next
                revHead.next = node
                node = tmp
            # 连接回来联系
            previous.next = revHead.next
            revTail.next = nextGroup
            previous = revTail
        return dummy.next
